import unittest
import wordgame

class MainTest(unittest.TestCase):

    def test_check_only_alpha(self):
        self.assertEqual(wordgame.check_only_alpha("01234"), False)

    def test_make_wordlist(self):
        words = wordgame.make_wordlist()
        # check words that are 5-letters are present
        self.assertIn("hello", words, "hello is not present")
        self.assertIn("queen", words, "queen is not present")
        self.assertIn("field", words, "field is not present")
        # check words that are not 5-letters are no present
        self.assertNotIn("fly", words, "fly is present")
        self.assertNotIn("letter", words, "letter is present")
        # check if nonsense 5-letter string is presnt
        self.assertNotIn("xlkjk", words, "xlkjk is present")

    def test_check_is_solved(self):
        self.assertTrue(wordgame.check_is_solved("hello", "hello"))
        self.assertFalse(wordgame.check_is_solved("hello", "field"))

