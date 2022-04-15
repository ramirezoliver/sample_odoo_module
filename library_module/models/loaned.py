from odoo import fields, models


class LoanedBook(models.Model):
    _name = 'library.loaned'
    _description = 'Library Loaned Book'

    book_id = fields.Many2one("library.book", required=True)
    user_id = fields.Many2one("library.user", required=True)
    loan_date = fields.Datetime('Loan Date', default=fields.Datetime.now, required=True)
    due_date = fields.Datetime('Due Date')