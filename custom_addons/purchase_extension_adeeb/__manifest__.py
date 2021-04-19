{
    'name': "Purchase Extension - Adeeb",
    'version': '1.0',
    'summary': "Purchase Extension - Adeeb",
    'sequence': 10,
    'description': """Extends Prurchase with Extra Functionality""",
    'depends': ['base',
                'purchase',
                'product_extension_adeeb'
                ],
    'data': [
        'views/purchase_extension_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
