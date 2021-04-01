from odoo import _, api, fields, models


class Quotations(models.Model):
    _inherit = "sale.order"

    note_on_customer = fields.Text("Note on Customer",
                                   help="Add Notes on Customers!")
