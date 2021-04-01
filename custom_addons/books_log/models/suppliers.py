from odoo import _, api, fields, models


class SupplierInheritance(models.Model):
    _inherit = 'res.partner'


class Suppliers(models.Model):
    _name = 'suppliers.logger'
    #_inherit = 'res.partner'
    _description = "First Addon - Supplier"
    #_rec_name = 'supplier_origin'

    # Extension

    # General
    supplier_origin = fields.Char(string="Origin")

    # Relations
    # test_id = fields.Many2one('')
