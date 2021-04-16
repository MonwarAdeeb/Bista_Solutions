from odoo import _, api, fields, models


class DealerName(models.Model):
    _name = 'dealer.product_brand_extension'
    _description = "Product Brand Ex - Dealer Name"
    _rec_name = "dealer_name"

    # General Fields
    dealer_name = fields.Char(string="Dealer Name")
