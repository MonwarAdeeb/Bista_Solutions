from odoo import _, api, fields, models


class ProductBrand(models.Model):
    _name = 'product_extension.brand'
    _description = "Product Extension - Product Brand"
    _rec_name = "brand"

    # General Fields
    brand = fields.Char(string="Brand")
