from odoo import _, api, fields, models


class ProductGroup(models.Model):
    _name = "test.product_group"
    _description = "Product Group"
    _rec_name = "name"
    _sql_constraints = [
        ('short_code_unique', 'unique(short_code)', 'Short Code Must be Unique!')
    ]

    name = fields.Char(string="Name", required=True)
    short_code = fields.Char(string="Short Code", required=True)
    parent_group = fields.Many2one(
        "test.product_group", string="Product Group")
