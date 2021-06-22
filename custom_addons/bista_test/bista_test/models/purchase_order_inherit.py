from odoo import _, api, fields, models


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    product_group = fields.Many2one(
        "test.product_group", string="Product Group")
    active_group_filter = fields.Boolean(string="Active Group Filter")
