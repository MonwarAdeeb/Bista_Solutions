from odoo import _, api, fields, models
from datetime import datetime, timedelta


class PurchaseOrderFilter(models.TransientModel):
    _name = "purchase.order.filter"
    _description = "Filter Class for Purchase Order"

    from_date = fields.Datetime(
        string='Date From', default=lambda self: fields.datetime.now())

    to_date = fields.Datetime(
        string='Date To', default=lambda self: fields.datetime.now())

    def filter_purchase_orders(self):
        # Creating list of date range selected in the UI
        selected_dates = [self.from_date + timedelta(days=x)
                          for x in range(0, (self.to_date-self.from_date).days+1)]

        # Creating empty list of order, date and filtered_order
        # for the purpose of storing respective filtered data
        order_list = []
        date_list = []
        filtered_list = []

        # Partially filtering orders from purchase.order.line
        # [taking non emptry received quantity values]
        filtered_orders = self.env["purchase.order.line"].search(
            [('qty_received', '>=', 1)])

        # This fully filters all valid orders from partially filtered orders
        # [billed quantity is less than received quantity]
        for order in filtered_orders:
            if order.qty_invoiced < order.qty_received:
                order_list.append(order)

        # Rerieving all objects from purchase.order to filter dates later
        filtered_dates = self.env["purchase.order"].search([])

        # This filters all valid dates
        for fdate in filtered_dates:
            if fdate.date_approve:
                date_order = fdate.date_approve.date()
                for sdate in selected_dates:
                    date_selected = sdate.date()
                    if date_order == date_selected:
                        date_list.append(fdate)

        # Filtering valid dates and orders by comparing then adding to filtered_list
        for item_o in order_list:
            for item_d in date_list:
                if item_o.order_id.id == item_d.id:
                    filtered_list.append(item_o.order_id.id)

        # Passing data through domain to the default views of the class
        return {
            'name': 'Purchase Order Filter',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', filtered_list)],
        }
