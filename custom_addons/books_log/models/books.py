from odoo import _, api, fields, models
from odoo.exceptions import UserError
from datetime import datetime


class Books(models.Model):
    _name = 'books.logger'
    _descroption = "First Addon - Books"
    _rec_name = 'title'

    # General Fields
    photo = fields.Binary(string="Cover Photo", attachment=True)
    title = fields.Char(string="Title", required=True,
                        help="This is the name of the book!")
    price = fields.Float(string="Price (In $)", required=True,
                         help="This is how much the book costs!")
    genre = fields.Char(string='Genre', default="Unspecified")
    pages = fields.Integer(string="Number of Pages")
    details = fields.Text("Details")
    date_of_purchase = fields.Date(
        string='Date of Purchase', default=datetime.today())

    # Computed Fieds
    discount_price = fields.Float(
        string="Discounted Price (In $)", compute="_get_discount", invisible=True, help="Price After 20% Discount!")
    book_code = fields.Char(string="Book Code", compute="_get_book_code")

    # Relations
    author = fields.Many2many('authors.logger', string="Author", required=True,
                              help="This is the one who wrote the book!")
    languages = fields.Many2one("languages.logger", string="Language")
    shelf_number = fields.Many2one('shelves.logger', string="Shelf")

    def generate_discount(self):
        after_discount = 0
        if self.price:
            after_discount = self.price * 0.80

        return after_discount

    def _get_discount(self):
        for item in self:
            item.discount_price = item.generate_discount()

    def generate_book_code(self):
        first_part = ""
        last_part = ""
        if self.title:
            first_part = self.title.split()[0]
        if self.genre:
            last_part = self.genre.split()[0]

        generated_code = first_part + '--' + last_part

        return generated_code

    def _get_book_code(self):
        for item in self:
            item.book_code = item.generate_book_code()

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
