{
    'name': "Books Logger",
    'version': '1.0',
    'summary': "First Custom Addon",
    'sequence': 10,
    'description': """Keeps Books' Details""",
    'depends': [],
    'data': [
        'views/books_view.xml',
        'views/authors_view.xml',
        'views/languages_view.xml',
        'views/shelves_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
