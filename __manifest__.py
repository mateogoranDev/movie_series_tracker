{
    'name': 'Cine & Series Tracker',
    'version': '18.0.1.0.1',
    'category': 'Tools',
    'summary': 'Gestiona tus películas y series favoritas, puntuaciones y catálogo personal con integración TMDB.',
    'author': 'mateogoranDev',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/movie_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'live_test_url': 'http://51.170.44.49:8069',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}