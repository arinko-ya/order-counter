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

        genre = Genre.query.get(1)

        item = {
            'name': 'test_item',
            'genre': genre,
            'price': 100,
            'is_high_priority': True}
        _ = Item.add_item(**item)

        self.assertTrue(Item.check_duplicate('test_item'))

    def test_add_item(self):
        Genre.add_genre('test_genre')
        genre = Genre.query.get(1)

        item = {
            'name': 'test_item',
            'genre': genre,
            'price': 100,
            'is_high_priority': True}

        result_succeeded = Item.add_item(**item)

        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        result_failed = Item.add_item(**item)

        self.assertEqual(result_failed.status, Status.FAILED)

    def test_update_item_name(self):
        Genre.add_genre('test_genre')
        genre = Genre.query.get(1)

        before_update_item = {
            'name': f'test_item_1',
            'genre': genre,
            'price': 100,
            'is_high_priority': True}
        _ = Item.add_item(**before_update_item)

        before_update_item['id'] = 1
        before_update_item['name'] = 'test_item_2'
        result_succeeded = Item.update(**before_update_item)
        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        fail_item = {
            'name': f'test_item_10',
            'genre': genre,
            'price': 100,
            'is_high_priority': True}
        _ = Item.add_item(**fail_item)

        fail_item['id'] = 2
        fail_item['name'] = 'test_item_2'
        result_failed = Item.update(**fail_item)
        self.assertEqual(result_failed.status, Status.FAILED)

    def test_update_is_active(self):
        Genre.add_genre('test_genre')
        genre = Genre.query.get(1)

        item = {
            'name': 'test_item',
            'genre': genre,
            'price': 100,
            'is_high_priority': True}
        _ = Item.add_item(**item)

        item['id'] = 1
        item['is_high_priority'] = False
        result = Item.update(**item)
        self.assertEqual(result.status, Status.SUCCEEDED)
