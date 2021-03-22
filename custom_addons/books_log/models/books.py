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
    price = fields.Float(string="Price (In $)", required=True,
                         help="This is how much the book costs!")
    discount_price = fields.Float(
        string="Discounted Price (In $)", compute="_get_discount", invisible=True, help="Price After 20% Discount!")
    genre = fields.Char(string='Genre', default="Unspecified")
    languages = fields.Many2one("languages.logger", string="Language")
    pages = fields.Integer(string="Number of Pages")
    date_of_purchase = fields.Date(
        string='Date of Purchase', default=datetime.today())
    shelf_number = fields.Many2one('shelves.logger', string="Shelf")
    book_code = fields.Char(string="Book Code", compute="_get_book_code")

    details = fields.Text("Details")

    def _get_discount(self):
        for item in self:
            after_discount = 0
            if item.price:
                after_discount = item.price * 0.75

            item.discount_price = after_discount

    def _get_book_code(self):
        for item in self:
            first_part = ""
            last_part = ""
            if item.title:
                first_part = item.title.split()[0]
            if item.genre:
                last_part = item.genre.split()[0]

            item.book_code = first_part + "-" + last_part

    @api.model
    def create(self, values):
        if values['price'] < 0 or values['pages'] < 0:
            raise UserError("Price or Number of Pages can't be negative!")

        if not values['details']:
            values['details'] = 'Not Available'

        return super(Books, self).create(values)

    def write(self, values):
        if 'details' in values.keys() and not values['details']:
            values['details'] = 'Deleted'

        return super(Books, self).write(values)

    @api.onchange('price', 'pages')
    def onchange_price_page(self):
        if self.price < 0 or self.pages < 0:
            raise UserError("Price or Number of Pages can't be negative!")
