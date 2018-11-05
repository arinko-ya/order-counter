import unittest

from app.tests.auth import TestAuth
from app.tests.genre import TestGenre
from app.tests.item import TestItem
from app.tests.order import TestOrder


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.makeSuite(TestAuth),
        unittest.makeSuite(TestGenre),
        unittest.makeSuite(TestItem),
        unittest.makeSuite(TestOrder)
    ])

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    print(runner.run(suite()).wasSuccessful())
