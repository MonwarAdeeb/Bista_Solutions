from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Banks(models.Model):
    _inherit = "res.partner"

    bank_name = fields.Many2one(
        "sp.bank_names", string="Bank Name")


class SalesOrderInherit(models.Model):
    _inherit = "sale.order"

    phone = fields.Char(string="Phone Number",
                        related="partner_id.phone", readonly=False)
    bank = fields.Many2one(
        "sp.bank_names", string="Bank", related="partner_id.bank_name")


class SalesOderLineInherit(models.Model):
    _inherit = "sale.order.line"

    branch = fields.Many2one("sp.branches", string="Branch")
