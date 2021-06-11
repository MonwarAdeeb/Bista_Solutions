from odoo import _, api, fields, models


class ProductInherit(models.Model):
    _inherit = "product.template"

    groups = fields.Many2one("test.product_group", string="Group")
    rating = fields.Selection([('one', "1"), ('two', "2"), ('three', "3"),
                               ('four', "4"), ('five', "5")], string="Rating", default="one")
