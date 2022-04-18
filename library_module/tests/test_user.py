from psycopg2 import IntegrityError
from odoo.tests.common import TransactionCase, tagged


USER_1 = {
    "name": 'user1',
}


@tagged('-standard', 'library1')
class TestUser(TransactionCase):
    def setUp(self):
        super(TestUser, self).setUp()

    def test_unique_book_constraint(self):
        with self.assertRaises(IntegrityError):
            self.env['library.user'].create(USER_1)
            self.env['library.user'].create(USER_1)
