from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char("Title", required=True)
    release_year = fields.Integer()
