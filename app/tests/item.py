import unittest

from app import db
from app.utils.log_util import Status
from app.item.models import Item
from app.genre.models import Genre


class TestItem(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_check_duplicate(self):
        Genre.add_genre('test_genre')
        self.assertFalse(Item.check_duplicate('test_item'))

        item = {
            'name': 'test_item',
            'genre_id': 1,
            'price': 100,
            'is_sale': True}
        _ = Item.add_item(**item)

        self.assertTrue(Item.check_duplicate('test_item'))

    def test_add_item(self):
        Genre.add_genre('test_genre')
        item = {
            'name': 'test_item',
            'genre_id': 1,
            'price': 100,
            'is_sale': True}
        result_succeeded = Item.add_item(**item)

        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        result_failed = Item.add_item(**item)

        self.assertEqual(result_failed.status, Status.FAILED)

    def test_update(self):
        Genre.add_genre('test_genre')
        item = {
            'name': 'test_item',
            'genre_id': 1,
            'price': 100,
            'is_sale': True}
        _ = Item.add_item(**item)

        item['id'] = 1

        item['name'] = 'test_item2'
        result_succeeded = Item.update(**item)
        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        item['name'] = 'test_item2'
        result_failed = Item.update(**item)
        self.assertEqual(result_failed.status, Status.FAILED)

        item['genre_id'] = 999
        result_failed_no_id = Item.update(**item)
        self.assertEqual(result_failed_no_id.status, Status.FAILED)
