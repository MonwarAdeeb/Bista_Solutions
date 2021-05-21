from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Doctors(models.Model):
    _name = "hms.doctors"
    _description = "Features for Doctors"

    # General Fields
    photo = fields.Binary(string="Photo", attachment=True)
    name = fields.Char(string="Name", required=True,
                       help="Enter Your Name Here")
    doctor_id = fields.Char(string="Doctor ID", required=True)
    date_of_joining = fields.Date(
        string="Date of Joining", default=datetime.today())
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
