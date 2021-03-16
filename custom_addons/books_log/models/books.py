from datetime import datetime

from odoo import _, api, fields, models


class Books(models.Model):
    _name = 'books.logger'
    _descroption = "First Addon - Books"
    _rec_name = 'title'

    photo = fields.Binary(string="Cover Photo", attachment=True)

    title = fields.Char(string="Title", required=True,
                        help="This is the name of the book!")
    author = fields.Many2many('authors.logger', string="Author", required=True,
                              help="This is the one who wrote the book!")
    price = fields.Float(string="Price in $", required=True,
                         help="This is how much the book costs!")
    genre = fields.Char(string='Genre')
    language = fields.Selection(
        [('bangla', 'Bangla'), ('english', 'English'), ('others', 'Other')], string='Language', default="bangla")
    pages = fields.Integer(string="Number of Pages")
    date_of_purchase = fields.Date(
        string='Date of Purchase', default=datetime.today())
    details = fields.Text("Details")
