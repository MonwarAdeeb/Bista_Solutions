from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class Doctors(models.Model):
    _inherit = "hms.doctors"
    _description = "Extra Features for Doctors"

    # General Fields
    speciality = fields.Char(
        string="Doctor's Speciality", help="Enter Your Speciality Here")
