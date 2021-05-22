from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Medicines(models.Model):
    _name = "hms.medicines"
    _description = "Features for Medicine"
    _rec_name = "name"

    # General Fields
    name = fields.Char(string="Medicine's Name", required=True,
                       help="Enter Your Name Here")

    description = fields.Text(string="Description")

    # Relational Field
    assigned_patients = fields.Many2many(
        "hms.patients", string="Assigned Patients")
