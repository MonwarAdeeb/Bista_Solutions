from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
import re


class ClientInherit(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, values):
        if values['email']:
            match = re.match(
                '^[_a-zA-Z0-9-]+(\.[_a-z0-9-]+)*@gmail+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', values['email'])
            if match:
                values['email'] = values['email'].lower()
                return super(ClientInherit, self).create(values)
            else:
                raise ValidationError('Please Enter a Valid Gmail ID')

    def write(self, values):
        if 'email' in values.keys() and values['email']:
            match = re.match(
                '^[_a-zA-Z0-9-]+(\.[_a-z0-9-]+)*@gmail+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', values['email'])
            if match:
                values['email'] = values['email'].lower()
                return super(ClientInherit, self).write(values)
            else:
                raise ValidationError('Please Enter a Valid Gmail ID')
