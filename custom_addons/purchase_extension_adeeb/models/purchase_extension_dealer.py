from odoo import _, api, fields, models


class PurchaseExtensionDealer(models.Model):
    _inherit = "purchase.order"

    dealer_id = fields.Many2one(
        "product_extension.dealer", string="Dealer Name")
    # product_id = fields.Many2one("product.template", string="Product")

    # @api.onchange('dealer_od')
    # def onchange_product_brand(self):
    #     if self.dealer_id:
    #         self.product_id = self.dealer_id.product_id.id
