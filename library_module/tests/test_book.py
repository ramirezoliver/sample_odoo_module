from psycopg2 import IntegrityError
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged
from datetime import datetime



@tagged('-standard', 'library1')
class TestBook(TransactionCase):
    def setUp(self):  
        super(TestBook, self).setUp()
        user1 = self.env.ref('library_module.sample_user1')
        self.book1 = self.env.ref('library_module.sample_book_free')
        self.loan_data = {
            "book_id": self.book1.id,
            "user_id": user1.id,
            "loan_date": '2012-01-01 23:59:59',
            "due_date": '',
        }


    def test_is_loaned(self):
        self.assertFalse(self.book1.is_loaned)
        self.env['library.loaned'].create(self.loan_data)
        self.assertTrue(self.book1.is_loaned)
