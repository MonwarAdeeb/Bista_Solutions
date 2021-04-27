{
    'name': "Purchase Order Filter",
    'version': '1.0',
    'summary': "Purchase Order Filter",
    'sequence': 1,
    'description': """Filters Purchase Order Based on Dates, Received & Billed""",
    'depends': ['base',
                'purchase',
                'sale',
                'stock',
                'contacts'
                ],
    'data': [
        'views/purchase_order_filter_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
