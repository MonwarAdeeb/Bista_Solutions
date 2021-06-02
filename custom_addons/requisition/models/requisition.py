from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Reqisition(models.Model):
    _name = "requisition.requisition"
    _description = "Requisitions"
    _rec_name = "employee_name"

    employee = fields.Many2one(
        "hr.employee", string="Employee Name", required=True, readonly=False)
    employee_name = fields.Char(string="Name", related="employee.name")
    date = fields.Date(string="Date of Requisition Request",
                       default=datetime.today(), readonly=False)
    state = fields.Selection([("draft", "Draft"), ("confirm", "Confirmed"), ("approve", "Approved"),
                              ("ready", "Ready"), ("receive", "Received")], string="state", default="draft")
    requisition_line = fields.One2many(
        'requisition.requisition.line', 'requisition_id', string='Requisition Line')

    def button_confirm(self):
        self.write({'state': 'confirm'})

    def button_approve(self):
        self.write({'state': 'approve'})

    def button_ready(self):
        self.write({'state': 'ready'})

    def button_receive(self):
        self.write({'state': 'receive'})


class RequisitionLine(models.Model):
    _name = "requisition.requisition.line"
    _description = "Requisitions Line"

    requisition_id = fields.Many2one(
        "requisition.requisition", string="Requisition Reference")
    products = fields.Many2one(
        "product.template", string="Product", required=True, readonly=False)
    quantity = fields.Float(string="Quantity", required=True, readonly=False)
