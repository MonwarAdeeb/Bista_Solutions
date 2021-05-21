from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Managements(models.Model):
    _name = "hms.managements"
    _description = "Features for Managements"
    _rec_name = "name"

    # General Fields
    photo = fields.Binary(string="Photo", attachment=True)
    name = fields.Char(string="Officer's Name", required=True,
                       help="Enter Your Name Here")
    officer_id = fields.Char(string="Managementt ID", required=True)
    date_of_joining = fields.Date(
        string="Date of Admission", default=datetime.today())
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
