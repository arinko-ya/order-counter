import unittest

from app import db
from app.utils.log_util import Status
from app.genre.models import Genre


class TestGenre(unittest.TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_check_duplicate(self):
        self.assertFalse(Genre.check_duplicate('test_genre'))
        Genre.add_genre('test_genre')
        self.assertTrue(Genre.check_duplicate('test_genre'))

    def test_add_genre(self):
        result_succeeded = Genre.add_genre('test_genre')
        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        result_failed = Genre.add_genre('test_genre')
        self.assertEqual(result_failed.status, Status.FAILED)

    def test_get_genre_list(self):
        self.assertEqual(len(Genre.get_genre_list()), 1)

        Genre.add_genre('test_genre1')
        Genre.add_genre('test_genre2')
        Genre.add_genre('test_genre3')

        self.assertEqual(len(Genre.get_genre_list()), 3)

    def test_update(self):
        Genre.add_genre('test_genre1')

        result_succeeded = Genre.update('1', 'test_genre2')
        self.assertEqual(result_succeeded.status, Status.SUCCEEDED)

        result_failed = Genre.update('1', 'test_genre2')
        self.assertEqual(result_failed.status, Status.FAILED)

        result_failed_no_id = Genre.update('999', 'test_genre999')
        self.assertEqual(result_failed_no_id.status, Status.FAILED)
