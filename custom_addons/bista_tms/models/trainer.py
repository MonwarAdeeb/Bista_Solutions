# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


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


class Location(models.Model):
    _name = "bista.location"
    _description = "Bista Training Management System - Locations"
    _rec_name = "location"

    location = fields.Char(string="Location")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country", required=True)


class Designation(models.Model):
    _name = "bista.trainee.role"
    _description = "Bista Training Management System - Designations"
    _rec_name = "designation"

    designation = fields.Char(string="Designation")
    sequence = fields.Integer(string="Sequence")
