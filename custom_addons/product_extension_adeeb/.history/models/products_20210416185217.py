from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Products(models.Model):
    _inherit = "product.template"
    _description = "Product Extension - Products"
    #_rec_name = "brand"

    # Relations
    brand = fields.Many2one("product_extension", string="Product Brand")
    dealer = fields.Many2one("dealer.product_extension", string="Dealer Name")
