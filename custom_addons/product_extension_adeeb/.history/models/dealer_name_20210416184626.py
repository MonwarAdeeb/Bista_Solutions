from odoo import _, api, fields, models


class DealerName(models.Model):
    _name = 'd'
    _description = "First Addon - Dealer Name"
    _rec_name = "dealer_name"

    # General Fields
    dealer_name = fields.Char(string="Dealer Name")
