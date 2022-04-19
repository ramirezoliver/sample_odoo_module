from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
import uuid

DEFAULT_LOAN_DURATION_DAYS = 7

class LoanedBook(models.Model):
    _name = 'library.loaned'
    _description = 'Library Loaned Book'

    name = fields.Char(size=36)
    book_id = fields.Many2one("library.book", required=True)
    user_id = fields.Many2one("library.user", required=True)
    loan_date = fields.Datetime('Loan Date', default=fields.Datetime.now, required=True)
    due_date = fields.Datetime('Due Date')
    
    _sql_constraints=[('book_id', 'unique(book_id)', 'Book already loaned')]

    @api.model
    def create(self, values):
        values['name'] = uuid.uuid4()
        datetime_format = '%Y-%m-%d %H:%M:%S'

        loan_date = datetime.strptime(values['loan_date'], datetime_format)
        if not values['due_date']:
            values['due_date'] = loan_date + timedelta(days=DEFAULT_LOAN_DURATION_DAYS)

        return super(LoanedBook, self).create(values)

    @api.constrains('due_date')
    def _check_due_date(self):
        for record in self:
            if record.loan_date > record.due_date:
                raise ValidationError("Due date cannot be later than loan date!")
