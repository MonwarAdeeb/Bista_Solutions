from odoo import _, api, fields, models


class Shelves(models.Model):
    _name = 'shelves.logger'
    _descroption = "First Addon - Shelves"
    _rec_name = 'shelf_no'

    shelf_no = fields.Integer(string="Shelf Number")
    books_in_shelf = fields.One2many(
        'books.logger', 'shelf_number', string="Books in Shelf")
