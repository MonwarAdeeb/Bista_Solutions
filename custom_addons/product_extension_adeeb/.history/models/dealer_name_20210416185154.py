from odoo import _, api, fields, models


class DealerName(models.Model):
    _name = 'product_extension.dealer'
    _description = "Product Extension - Dealer Name"
    _rec_name = "dealer_name"

    # General Fields
    dealer_name = fields.Char(string="Dealer Name")
