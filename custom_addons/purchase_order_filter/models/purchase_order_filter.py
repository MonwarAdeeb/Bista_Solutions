from odoo import _, api, fields, models
from datetime import datetime, timedelta


class PurchaseOrderFilter(models.TransientModel):
    _name = "purchase.order.filter"
    _description = "Filter Class for Purchase Order"

    from_date = fields.Date(
        string='Date From', default=datetime.today())
    to_date = fields.Date(
        string='Date To', default=datetime.today())

    def filter_purchase_orders(self):
        order_list = []
        date_list = []
        filtered_list = []

        # Partially filtering orders from purchase.order.line to reduce data overhead
        # [taking non emptry received quantity values]
        filtered_orders = self.env["purchase.order.line"].search(
            [('qty_received', '>=', 1)])

        # This fully filters all valid orders IDs from partially filtered_orders
        # [billed quantity is less than received quantity]
        for order in filtered_orders:
            if order.qty_invoiced < order.qty_received:
                order_list.append(order.order_id.id)

        # Rerieving all objects from purchase.order in selected date range
        filtered_dates = self.env["purchase.order"].search(
            ['&', ('date_approve', '>=', self.from_date), ('date_approve', '<=', self.to_date)])

        # Retreiving IDs of Valid Dates
        for date in filtered_dates:
            date_list.append(date.id)

        # Filtering valid dates and orders by comparing their IDs,
        # Then adding to filtered_list
        for item_o in order_list:
            for item_d in date_list:
                if item_o == item_d:
                    filtered_list.append(item_o)

        # Passing data through domain to the default views of the class
        return {
            'name': 'Purchase Order Filter',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', filtered_list)],
        }
