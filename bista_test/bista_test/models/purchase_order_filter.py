from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class PurchaseOrderFilter(models.TransientModel):
    _name = "purchase.order.filter"

    customers = fields.Many2many("res.partner", string="Customers")
    # customer_ids = user.sudo().customers.ids

    def filter_purchase_order(self):

        return {
            'name': "purchase filter",
            'type': "ir.actions.act_window",
            'res_model': "purchase.order",
            'view_mode': "tree,form",
            'domain': [('partner_id.id', 'in', self.customers.ids)],
        }
