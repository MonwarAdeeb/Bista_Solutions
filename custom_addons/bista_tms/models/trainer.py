# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Trainer(models.Model):
    _name = "bista.trainer"
    _description = "Bista Training Management System - Trainer"
    _rec_name = "name"

    profile_image = fields.Binary(string="Profile Image", attachement=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string="Name", compute="_get_name", store=True)

    @api.depends('first_name', 'last_name')
    def _get_name(self):
        for record in self:
            if record.last_name:
                record.name = record.first_name + ' ' + record.last_name
            else:
                record.name = record.first_name
