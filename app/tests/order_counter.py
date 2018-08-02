import unittest

from app import db
from app.genre.models import Genre
from app.item.models import Item


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

        Item.update(**item)

        changed_item = Item.query.filter_by(id=item['id']).first()
        changed_item = changed_item.__dict__

        for item_key in item.keys():
            with self.subTest(item_key=item_key):
                self.assertEqual(changed_item[item_key], item[item_key])
