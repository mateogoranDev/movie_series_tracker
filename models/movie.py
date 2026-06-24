import requests
import base64
from odoo import models, fields, api
from odoo.exceptions import UserError

class MovieGenre(models.Model):
    _name = 'movie.genre'
    _description = 'Géneros de Películas y Series'
    
    name = fields.Char(string='Género', required=True)
    color = fields.Integer(string='Color') # Para que tengan colores en la UI

class MovieMedia(models.Model):
    _name = 'movie.media'
    _description = 'Películas y Series'
    _order = 'release_year desc, name'

    name = fields.Char(string='Título', required=True)
    media_type = fields.Selection([
        ('movie', 'Película'),
        ('series', 'Serie')
    ], string='Tipo', default='movie', required=True)
    
    release_year = fields.Integer(string='Año de Estreno')
    
    # NUEVO: Ahora es un campo de etiquetas de colores
    genre_ids = fields.Many2many('movie.genre', string='Géneros')
    
    synopsis = fields.Text(string='Sinopsis')
    watched = fields.Boolean(string='¿Vista?', default=False)
    image = fields.Binary(string='Carátula')

    rating = fields.Selection([
        ('0', 'Sin puntuación'),
        ('1', 'Mala'),
        ('2', 'Entretenida'),
        ('3', 'Buena'),
        ('4', 'Muy Buena'),
        ('5', 'Obra Maestra')
    ], string='Puntuación', default='0')

    tmdb_api_key = fields.Char(string='TMDB API Key', compute='_compute_tmdb_api_key', inverse='_inverse_tmdb_api_key', store=False)

    def _compute_tmdb_api_key(self):
        key = self.env['ir.config_parameter'].sudo().get_param('movie_series_tracker.tmdb_api_key') or ''
        for record in self:
            record.tmdb_api_key = key

    def _inverse_tmdb_api_key(self):
        for record in self:
            if record.tmdb_api_key:
                self.env['ir.config_parameter'].sudo().set_param('movie_series_tracker.tmdb_api_key', record.tmdb_api_key.strip())

    def action_tmdb_signup(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.themoviedb.org/signup',
            'target': 'new',
        }

    def action_fetch_tmdb_info(self):
        self.ensure_one()
        if not self.name:
            raise UserError("¡Primero escribe un título para buscar!")

        api_key = self.env['ir.config_parameter'].sudo().get_param('movie_series_tracker.tmdb_api_key')
        if not api_key:
            raise UserError("Por favor, introduce tu API Key antes de buscar.")
        
        endpoint = "movie" if self.media_type == 'movie' else "tv"
        url = f"https://api.themoviedb.org/3/search/{endpoint}"
        
        params = {
            'api_key': api_key,
            'query': self.name,
            'language': 'es-ES'
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])
                
                if not results:
                    raise UserError(f"No se encontró nada en TMDB con el nombre '{self.name}'.")
                
                item = results[0]
                self.synopsis = item.get('overview', '')
                
                date_field = 'release_date' if self.media_type == 'movie' else 'first_air_date'
                full_date = item.get(date_field, '')
                if full_date:
                    self.release_year = int(full_date.split('-')[0])
                
                poster_path = item.get('poster_path')
                if poster_path:
                    image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                    img_response = requests.get(image_url, timeout=10)
                    if img_response.status_code == 200:
                        self.image = base64.b64encode(img_response.content)

                # 🌟 NUEVO: Mapeo automático de géneros desde TMDB
                # Obtenemos la lista de géneros oficial de TMDB para poner nombres en vez de IDs numéricos
                gen_url = f"https://api.themoviedb.org/3/genre/{endpoint}/list"
                gen_response = requests.get(gen_url, params={'api_key': api_key, 'language': 'es-ES'}, timeout=10)
                if gen_response.status_code == 200:
                    tmdb_genres = {g['id']: g['name'] for g in gen_response.json().get('genres', [])}
                    item_genre_ids = item.get('genre_ids', [])
                    
                    odoo_genre_ids = []
                    for g_id in item_genre_ids:
                        g_name = tmdb_genres.get(g_id)
                        if g_name:
                            # Buscamos si el género ya existe en nuestra BD, si no, lo creamos
                            genre_record = self.env['movie.genre'].sudo().search([('name', '=', g_name)], limit=1)
                            if not genre_record:
                                # Le asignamos un color aleatorio entre 1 y 11 para Odoo
                                genre_record = self.env['movie.genre'].sudo().create({'name': g_name, 'color': (g_id % 11) + 1})
                            odoo_genre_ids.append(genre_record.id)
                    
                    # Asignamos las etiquetas al registro
                    self.genre_ids = [(6, 0, odoo_genre_ids)]

            else:
                raise UserError(f"API Key inválida o error con TMDB (Código {response.status_code}).")
        except requests.exceptions.RequestException:
            raise UserError("No se pudo conectar a internet o a la API de TMDB.")