from odoo import _, api, fields, models
from odoo.exceptions import UserError
import re


class Languages(models.Model):
    _name = 'languages.logger'
    _descroption = "First Addon - Languages"
    _rec_name = "languages"

    languages = fields.Char(string="Languages")
    pattern = "\d"

    @api.model
    def create(self, value):
        if re.findall(self.pattern, value['languages']):
            raise UserError("Language name can't contain any numbers!")

        return super(Languages, self).create(value)

    def write(self, value):
        if re.findall(self.pattern, value['languages']):
            raise UserError("Language name can't contain any numbers!")

        return super(Languages, self).write(value)

    @api.onchange('languages')
    def onchange_language(self):
        if self.languages and re.findall(self.pattern, self.languages):
            raise UserError("Language name can't contain any numbers!")
