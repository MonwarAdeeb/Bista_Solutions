# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
import uuid


class Trainee(models.Model):
    _name = "bista.trainee"
    _description = "Bista Training Management System - Trainee"
    _rec_name = 'name'
    _sql_constraints = [
        ('trainee_id_unique', 'unique(trainee_id)', 'Trainee ID must be unique!')
    ]

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string="Name", compute="_get_name", store=True)
    trainee_id = fields.Char(string="Trainee ID", readonly=True)
    emp_code = fields.Char(string="EMP Code")
    email = fields.Char(string="Personal Email ID", required=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", default="male")
    date_of_birth = fields.Datetime(
        string="Date of Birth", default=datetime.today())
    date_of_joining = fields.Datetime(
        string="Date of Joining", default=datetime.today())
    location = fields.Many2one("bista.location", string="Location")
    designation = fields.Many2one("bista.trainee.role", string="Designation")
    status = fields.Selection(
        [('new', 'New'), ('training', 'Training'),
         ('rejected', 'Rejected'), ('employeed', 'Employeed')],
        string="Status", default="new")
    profile_image = fields.Binary(string="Profile Image", attachement=True)

    @api.depends('first_name', 'last_name')
    def _get_name(self):
        for record in self:
            if not record.first_name:
                record.first_name = ''
            if record.last_name:
                record.name = record.first_name + ' ' + record.last_name
            else:
                record.name = record.first_name

    @api.model
    def create(self, values):
        values['trainee_id'] = uuid.uuid4().hex[:4]
        return super(Trainee, self).create(values)

    @api.onchange('date_of_birth')
    def onchange_date_of_birth(self):
        if self.date_of_birth > datetime.today():
            raise ValidationError(_("Future Dates are not Allowed!"))
