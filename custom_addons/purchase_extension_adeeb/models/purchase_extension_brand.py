from odoo import _, api, fields, models


class PurchaseExtensionBrand(models.Model):
    _inherit = 'purchase.order.line'
    # _inherit = ['purchase.order', 'purchase.order.line']

    brand_id = fields.Many2one(
        "product_extension.brand", string="Brand")

    @api.onchange('product_id')
    def onchange_product_brand(self):
        if self.product_id:
            self.brand_id = self.product_id.brand.id
