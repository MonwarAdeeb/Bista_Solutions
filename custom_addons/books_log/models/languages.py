from odoo import _, api, fields, models


class Languages(models.Model):
    _name = 'languages.logger'
    _descroption = "First Addon - Languages"
    _rec_name = 'languages'

    languages = fields.Char(string="Languages")
    # books = fields.One2many('books.logger', 'title',
    #                         string="Books in This Language")
