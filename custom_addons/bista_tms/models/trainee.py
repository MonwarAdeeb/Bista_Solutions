# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
import uuid


class Trainee(models.Model):
    _name = "bista.trainee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bista Training Management System - Trainee"
    _rec_name = 'name'

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string="Name", compute="_get_name", store=True)
    trainee_id = fields.Char(string="Trainee ID", readonly=True)
    emp_code = fields.Char(string="EMP Code")
    email = fields.Char(string="Personal Email ID", required=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", default="male")
    date_of_birth = fields.Date(
        string="Date of Birth", default=lambda self: fields.datetime.today())
    date_of_joining = fields.Date(
        string="Date of Joining", default=lambda self: fields.datetime.today())
    location = fields.Many2one("bista.location", string="Location")
    designation = fields.Many2one("bista.trainee.role", string="Designation")
    status = fields.Selection(
        [('new', 'New'), ('training', 'Training'),
         ('rejected', 'Rejected'), ('employeed', 'Employeed')],
        string="Status", default="new")
    profile_image = fields.Image(string="Profile Image", attachement=True)
    sequence = fields.Char(string="Sequence", required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    state = fields.Selection([('unconfirmed', "Unconfirmed"),
                              ('confirmed', "Confirmed")], string="State", default="unconfirmed")


    _sql_constraints = [
        ('trainee_id_unique', 'unique(trainee_id)', 'Trainee ID must be unique!')
    ]

    @api.depends('first_name', 'last_name')
    def _get_name(self):
        for record in self:
            # if not record.first_name:
            #     record.first_name = ''
            if record.last_name:
                record.name = "%s %s" % (record.first_name, record.last_name)
            else:
                record.name = "%s" % (record.first_name)

    @api.model
    def create(self, values):
        values['trainee_id'] = uuid.uuid4().hex[:4]

        if values.get('sequence', ('New')) == ('New'):
            values['sequence'] = self.env['ir.sequence'].next_by_code(
                'bista.trainee.sequence') or _('New')

        return super(Trainee, self).create(values)

    @api.onchange('date_of_birth')
    def onchange_date_of_birth(self):
        if self.date_of_birth > datetime.today().date():
            raise ValidationError(_("Future Dates are not Allowed!"))

    def action_create_employee(self):
        self.write({'state': 'confirmed'})
        self.env['hr.employee'].create(dict(
            name=self.name,
            image_1920=self.profile_image,
            job_title=self.designation.designation,
            private_email=self.email,
            gender=self.gender,
        ))
