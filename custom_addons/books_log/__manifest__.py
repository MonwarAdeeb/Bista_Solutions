{
    'name': "Books Logger",
    'version': '1.0',
    'summary': "First Custom Addon",
    'sequence': 10,
    'description': """Keeps Books' Details""",
    'depends': ['base',
                'contacts',
                'sale'
                ],
    'data': [
        'security/book_log_security.xml',
        'security/ir.model.access.csv',

        'views/books_view.xml',
        'views/authors_view.xml',
        'views/languages_view.xml',
        'views/shelves_view.xml',
        'views/quotations_view.xml',
        'views/product_brand_view.xml',
        'views/dealer_name_view.xml',
        'views/products_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
