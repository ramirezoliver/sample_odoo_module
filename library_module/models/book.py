from odoo import api, fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char("Title", required=True)
    release_year = fields.Integer()
    loaned_ids = fields.One2many("library.loaned", "book_id", string="Book Loan")
    image = fields.Binary("Book Image", attachment=True)
    is_loaned = fields.Boolean(compute='_is_loaned',
                                 store=True,
                                 string="Is loaned",
                                 readonly=True)

    @api.depends('loaned_ids')
    def _is_loaned(self):
        for book in self:
            book.is_loaned = len(book.loaned_ids) > 0
