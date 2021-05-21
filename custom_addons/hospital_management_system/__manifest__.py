{
    "name": "Hospital Management System",
    "version": "1.0",
    "summary": "This is a Simple Management System for a Hospital",
    "sequence": 10,
    "description": "Hospital Management System including Features for Doctors, Patients and Management",
    "depends": [
        "base"
    ],
    "data": [
        "security/hms_security.xml",
        "security/ir.model.access.csv",

        "views/doctors_views.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,

}
