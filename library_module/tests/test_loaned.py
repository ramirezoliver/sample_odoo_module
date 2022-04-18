from psycopg2 import IntegrityError
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged
from datetime import datetime

BOOK_1 = {
    "name": 'Moby-Dick',
    "release_year": 1994,
}

USER_1 = {
    "name": 'user1',
}



@tagged('-standard', 'library1')
class TestLoan(TransactionCase):
    def setUp(self):
        super(TestLoan, self).setUp()
        user1 = self.env['library.user'].create(USER_1)
        book1 = self.env['library.book'].create(BOOK_1)
        self.loan_data = {
            "book_id": book1.id,
            "user_id": user1.id,
            "loan_date": '2012-01-01 23:59:59',
            "due_date": '',
        }

    def test_due_date_earlier_than_loan_date(self):
        self.loan_data['due_date'] = '2011-12-31 23:59:59'
        with self.assertRaises(ValidationError):
            self.env['library.loaned'].create(self.loan_data)

    def test_valid_due_date(self):
        self.loan_data['due_date'] = '2013-12-31 23:59:59'
        self.env['library.loaned'].create(self.loan_data)


    def test_blank_due_date(self):
        datetime_format = '%Y-%m-%d %H:%M:%S'

        self.loan_data['due_date'] = ''
        record = self.env['library.loaned'].create(self.loan_data)

        self.assertEqual(
            record.due_date, 
            datetime.strptime('2012-01-08 23:59:59', datetime_format)
        )


    def test_unique_book_constraint(self):
        with self.assertRaises(IntegrityError):
            self.env['library.loaned'].create(self.loan_data)
            self.env['library.loaned'].create(self.loan_data)
