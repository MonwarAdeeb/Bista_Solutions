from odoo import _, api, fields, models


class PurchaseExtensionDealer(models.Model):
    _inherit = "purchase.order"

    dealer_id = fields.Many2one(
        "product_extension.dealer", string="Dealer Name")
