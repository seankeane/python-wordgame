import unittest
from helper import check_only_alpha


class MainTest(unittest.TestCase):

    def test_check_only_alpha(self):
        result = check_only_alpha("01234")
        self.assertEqual(result, False)
