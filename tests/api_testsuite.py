import unittest

from tests.test_case_movie_api import TestMovieAPI
from tests.test_case_quote_api import TestQuoteAPI


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMovieAPI))
    suite.addTest(unittest.makeSuite(TestQuoteAPI))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
