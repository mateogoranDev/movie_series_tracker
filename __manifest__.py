{
    'name': 'Cine & Series Tracker',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Gestiona tus películas y series favoritas, puntuaciones y catálogo personal con integración TMDB.',
    'author': 'mateogoranDev',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/movie_views.xml',
    ],
    'images': ['static/description/banner.png'],  # Opcional: ayuda a las tiendas a previsualizar tu módulo
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}