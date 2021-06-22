from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class BankNames(models.Model):
    _name = "sp.bank_names"
    _description = "Banks"
    _rec_name = "bank_name"

    bank_name = fields.Char(string="Bank Name")
    branches = fields.One2many(
        "sp.branches", "bank", string="Branches of this Bank")


class BankBranches(models.Model):
    _name = "sp.branches"
    _description = "Branches"
    _rec_name = "branch_name"

    branch_name = fields.Char(string="Branch Name")
    bank = fields.Many2one("sp.bank_names", string="Bank Name")
