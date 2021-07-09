{
    'name': "Bista Training Management System",
    'version': '1.0',
    'summary': "",
    'sequence': 10,
    'description': """Practice - Lithin Sir""",
    'depends': ['base',
                'mail',
                'hr',
                'sale',
                'contacts',
                'stock',
                ],
    'data': [
        'security/bista_tms_security.xml',
        'security/bista_tms_record_rules.xml',
        'security/ir.model.access.csv',

        'views/trainee_view.xml',
        'views/trainer_view.xml',
        'views/designation_view.xml',
        'views/location_view.xml',
        'views/training_view.xml',

        'data/ir_sequence_data.xml',

        'report/bista_tms_report.xml',

        'wizard/bista_tms_trainee_filter_wizard.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
