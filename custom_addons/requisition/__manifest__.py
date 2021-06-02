{
    'name': "Requisition",
    'version': '1.0',
    'summary': "Features Requisitions Procedure of Employees to HR",
    'sequence': 10,
    'description': """Provides Features for Requisition of Employees to HR""",
    'depends': ['base',
                'hr',
                'sale',
                'purchase',
                'stock',
                ],
    'data': [
        'security/requisition_security.xml',
        'security/ir.model.access.csv',

        'views/requisition_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
