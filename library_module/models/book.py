from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char("Title", required=True)
    release_year = fields.Integer()
    loaned_ids = fields.One2many("library.loaned", "book_id", string="Book Loan")
