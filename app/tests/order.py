import unittest
from datetime import datetime

from app import db
from app.genre.models import Genre
from app.item.models import Item
from app.order.models import Order
from app.order import registration
from app.utils.log_util import Status


class TestOrder(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

        Genre.add_genre('test_genre')
        self.genre = Genre.query.filter_by(name='test_genre').first()
        add_item = {
            'name': 'test_item',
            'genre': self.genre,
            'price': 100,
            'is_active': True,
            'is_high_priority': True}
        Item.add_item(**add_item)

        self.item = Item.query.filter_by(name='test_item').first()
        self.today = datetime.today().date()

        db.session.add(Order(
            item=self.item, price=self.item.price * 3,
            quantity=3, sold_at=self.today)
        )
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_add_order(self):
        result = registration.save_order([{
            'item': self.item, 'quantity': 2, 'sold_at': self.today}])
        self.assertEqual(result.status, Status.SUCCEEDED)

        order = Order.query.all()
        self.assertEqual(len(order), 2)

    def test_add_multi_order(self):
        add_item = {
            'name': 'test_item_2',
            'genre': self.genre,
            'price': 100,
            'is_active': True,
            'is_high_priority': True}
        Item.add_item(**add_item)
        item2 = Item.query.filter_by(name='test_item_2').first()

        result = registration.save_order([
            {'item': self.item, 'quantity': 2, 'sold_at': self.today},
            {'item': item2, 'quantity': 2, 'sold_at': self.today}
        ])
        self.assertEqual(result.status, Status.SUCCEEDED)

        order = Order.query.all()
        self.assertEqual(len(order), 3)

    def test_add_no_quantity(self):
        add_item = {
            'name': 'test_item_2',
            'genre': self.genre,
            'price': 100,
            'is_active': True,
            'is_high_priority': True}
        Item.add_item(**add_item)
        item2 = Item.query.filter_by(name='test_item_2')

        result = registration.save_order([{
            'item': item2, 'quantity': 0, 'sold_at': self.today}])
        self.assertEqual(result.status, Status.FAILED)

        order = Order.query.all()
        self.assertEqual(len(order), 1)
