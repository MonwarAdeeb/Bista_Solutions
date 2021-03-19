from datetime import datetime
from odoo import _, api, fields, models


class Authors(models.Model):
    _name = 'authors.logger'
    _descroption = "First Addon - Author"
    _rec_name = 'name'

    photo_author = fields.Binary(string="Photo", attachment=True)

    name = fields.Char(string="Name", required=True,
                       help="This is the name of the Author!")
    date_of_birth = fields.Date(
        string='Date of Birth', default=datetime.today())
    published_books = fields.Many2many(
        'books.logger', string="Published Books")
