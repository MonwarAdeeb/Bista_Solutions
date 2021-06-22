{
    'name': "Sales Practice",
    'version': '1.0',
    'summary': "This Module is to Practice Sales",
    'sequence': 10,
    'description': """This Module is to Practice Sales""",
    'depends': ['base',
                'sale_management',
                'purchase',
                'stock',
                'contacts',
                ],
    'data': [
        'security/sales_practice_security.xml',
        'security/ir.model.access.csv',

        'views/sales_practice_view.xml',
        'views/sales_practice_inherit_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
