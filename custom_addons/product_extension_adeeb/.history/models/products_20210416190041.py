from odoo import _, api, fields, models


class Products(models.Model):
    _inherit = "product.template"
    _description = "Product Extension - Products"
    #_rec_name = "brand"

    # Relations
    brand = fields.Many2one("product_extension.brand", string="Product Brand")
    dealer = fields.Many2one("product_extension.dealer", string="Dealer Name")
