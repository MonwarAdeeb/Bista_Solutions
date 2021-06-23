# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Designation(models.Model):
    _name = "bista.trainee.role"
    _description = "Bista Training Management System - Designations"
    _rec_name = "designation"

    designation = fields.Char(string="Designation")
    sequence = fields.Integer(string="Sequence")
