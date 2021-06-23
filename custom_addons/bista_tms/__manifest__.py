{
    'name': "Bista Training Management System",
    'version': '1.0',
    'summary': "",
    'sequence': 10,
    'description': """Practice - Lithin Sir""",
    'depends': ['base',
                ],
    'data': [
        'security/bista_tms_security.xml',
        'security/ir.model.access.csv',

        'views/trainee_view.xml',
        'views/trainer_view.xml',
        'views/designation_view.xml',
        'views/location_view.xml',
        'views/training_view.xml',

        # 'views/_view.xml',

        # 'report/_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
