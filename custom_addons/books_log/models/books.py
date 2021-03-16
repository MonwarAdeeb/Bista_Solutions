from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import datetime


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
    genre = fields.Char(string='Genre', default="Unspecified")
    languages = fields.Many2one("languages.logger", string="Language")
    # language = fields.Selection(
    #     [('bangla', 'Bangla'), ('english', 'English'), ('others', 'Other')], string='Language', default="bangla")
    pages = fields.Integer(string="Number of Pages")
    date_of_purchase = fields.Date(
        string='Date of Purchase', default=datetime.today())
    details = fields.Text("Details")

    @api.model
    def create(self, values):
        if values['price'] < 0 or values['pages'] < 0:
            raise UserError("Price or Number of Pages can't be negative!")

        if not values['details']:
            values['details'] = 'Not Available'
        return super(Books, self).create(values)

    def write(self, values):
        if values['price'] < 0 or values['pages'] < 0:
            raise UserError("Price or Number of Pages can't be negative!")

        if not values['details']:
            values['details'] = 'Not Available'
        return super(Books, self).write(values)

    @api.onchange('price', 'pages')
    def onchange_price_page(self):
        if self.price < 0 or self.pages < 0:
            raise UserError("Price or Number of Pages can't be negative!")
