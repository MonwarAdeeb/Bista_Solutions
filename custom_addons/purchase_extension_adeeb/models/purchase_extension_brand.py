from odoo import _, api, fields, models


class PurchaseExtensionBrand(models.Model):
    _inherit = 'purchase.order.line'
    # _inherit = ['purchase.order', 'purchase.order.line']

    brand_id = fields.Many2one(
        "product_extension.brand", string="Brand", readonly=True)

    @api.onchange('product_id')
    def onchange_product_brand(self):
        if self.product_id:
            self.brand_id = self.product_id.brand.id

    def write(self, values):
        values['brand_id'] = self.product_id.brand.id
        result = super(PurchaseExtensionBrand, self).write(values)
        return result
