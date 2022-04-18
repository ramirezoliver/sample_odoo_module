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
class TestBook(TransactionCase):
    def setUp(self):
        super(TestLoan, self).setUp()
        user1 = self.env['library.user'].create(USER_1)
        self.book1 = self.env['library.book'].create(BOOK_1)
        self.loan_data = {
            "book_id": self.book1.id,
            "user_id": user1.id,
            "loan_date": '2012-01-01 23:59:59',
            "due_date": '',
        }


    def test_is_loaned(self):
        self.assertFalse(self.book1.is_loaned)
        self.env['library.loaned'].create(loan_data)
        self.assertTrue(self.book1.is_loaned)
