from odoo import _, api, fields, models
from odoo.exceptions import UserError


class DealerName(models.Model):
    _name = 'dealer_name.logger'
    _description = "First Addon - Dealer Name"
    _rec_name = "dealer_name"

    # General Fields
    dealer_name = fields.Char(string="Dealer Name")
