{
    'name': "Product Extension - Adeeb",
    'version': '1.0',
    'summary': "Product Extension - Adeeb",
    'sequence': 10,
    'description': """Extends Products with Brand & Dealer""",
    'depends': ['base',
                'contacts',
                'sale'
                ],
    'data': [
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