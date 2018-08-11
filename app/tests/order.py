import unittest

from app import db
from app.order.models import Order
from app import input_data


class TestOrder(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()
        input_data.main()

    def tearDown(self):
        db.drop_all()

    def test_add_order(self):
        user = User('test_user')
        user.set_password('password')

        self.assertNotEqual(user.password, 'password')

    def test_user_check_password(self):
        user = User('test_user')
        user.set_password('password')

        self.assertTrue(user.check_password('password'))

    def test_user_create(self):
        User.create('test_user', 'password')
        user = User.query.filter_by(name='test_user').first()

        self.assertTrue(user)
