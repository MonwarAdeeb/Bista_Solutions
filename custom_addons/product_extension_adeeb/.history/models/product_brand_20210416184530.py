from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductBrand(models.Model):
    _name = 'product_brand_extension.'
    _description = "First Addon - Product Brand"
    _rec_name = "brand"

    # General Fields
    brand = fields.Char(string="Brand")
