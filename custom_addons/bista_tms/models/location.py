# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Location(models.Model):
    _name = "bista.location"
    _description = "Bista Training Management System - Locations"
    _rec_name = "location"

    location = fields.Char(string="Location")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    state = fields.Many2one('res.country.state', string='State')
    country = fields.Many2one('res.country', string='Country', required=True)
