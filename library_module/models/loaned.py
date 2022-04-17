from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class LoanedBook(models.Model):
    _name = 'library.loaned'
    _description = 'Library Loaned Book'

    book_id = fields.Many2one("library.book", required=True)
    user_id = fields.Many2one("library.user", required=True)
    loan_date = fields.Datetime('Loan Date', default=fields.Datetime.now, required=True)
    due_date = fields.Datetime('Due Date')
    
    _sql_constraints=[('book_id', 'unique(book_id)', 'Book already loaned')]

    @api.model
    def create(self, values):
        datetime_format = '%Y-%m-%d %H:%M:%S'

        loan_date = datetime.strptime(values['loan_date'], datetime_format)
        if not values['due_date']:
            values['due_date'] = loan_date + timedelta(days=7)
        else:
            due_date = datetime.strptime(values['due_date'], datetime_format)
            if loan_date > due_date:
                raise ValidationError("Due date cannot be later than loan date")

        return super(LoanedBook, self).create(values)
