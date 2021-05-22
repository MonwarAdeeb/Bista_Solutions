from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Patients(models.Model):
    _name = "hms.patients"
    _description = "Features for Patients"
    _rec_name = "name"

    # General Fields
    photo = fields.Binary(string="Photo", attachment=True)
    name = fields.Char(string="Patient's Name", required=True,
                       help="Enter Your Name Here")
    patient_id = fields.Char(string="Patient ID", required=True)
    date_of_admission = fields.Datetime(
        string="Date of Admission", default=datetime.now())
    symptoms = fields.Text(string="Symptoms")
    diagnosis = fields.Text(string="Diagnostics")
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")

    # Relational Fields
    assigned_doctor = fields.Many2one("hms.doctors", string="Assigned Doctor")
    assigned_medicines = fields.Many2many(
        "hms.medicines", string="Assigned Medicines")
