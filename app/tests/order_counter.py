import unittest

from app import db
from app.models import Genre, Item


class TestOrderCounter(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_update_item(self):
        db.session.add_all([Genre(name='test_genre'),
                            Genre(name='test_genre2')])
        db.session.add(Item('test_item', '1', 100, True))
        db.session.commit()
        item = {'id': 1,
                'name': 'test_item2',
                'genre_id': 2,
                'price': 200,
                'is_sale': False}

        Item.update_item(**item)

        changed_item = Item.query.filter_by(id=item['id']).first()

        self.assertEqual(changed_item.name, item['name'])
        self.assertEqual(changed_item.genre_id, item['genre_id'])
        self.assertEqual(changed_item.price, item['price'])
        self.assertEqual(changed_item.is_sale, item['is_sale'])
