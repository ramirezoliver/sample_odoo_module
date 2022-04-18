from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestLoanConstrains(TransactionCase):
    def setUp(self):
        user1 = self.env.ref("library.sample_user1")
        book1 = self.env.ref("library.sample_book_free")
        self.loan_data = {
            'user_id': user1,
            'book_id': book1
        }
    
    def test_valid_loan(self):
        self.loan_data['loan_date'] = '2012-12-31 23:59:59'
        self.loan_data['loan_date'] = '2011-12-31 23:59:59'
        with self.assertRaises(ValidationError):
            self.env['library.loaned'].create(self.loan_data)
