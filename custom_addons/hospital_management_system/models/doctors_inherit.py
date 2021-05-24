from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class Doctors(models.Model):
    # Inheriting 'hms.doctors' Model
    _inherit = "hms.doctors"
    _description = "Extra Features for Doctors"

    # General Fields to add to parent model
    speciality = fields.Char(
        string="Doctor's Speciality", help="Enter Your Speciality Here")
