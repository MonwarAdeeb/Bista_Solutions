{
    'name': "Bista Test - Adeeb",
    'version': '1.0',
    'summary': "",
    'sequence': 10,
    'description': """Bista Test""",
    'depends': ['base',
                'contacts',
                'sale',
                'purchase',
                'stock',
                'sale_management',
                ],
    'data': [
        'security/bista_test_security.xml',
        'security/ir.model.access.csv',

        'views/product_group_view.xml',
        'views/product_template_inherit.xml',
        'views/purchase_order_inherit_view.xml',
        'views/purchase_order_filter_view.xml',
        # 'views/sale_order_inherit_view.xml',

        'report/test_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
