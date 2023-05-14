import unittest
import json

from translator import english_to_french, french_to_english

class TestEnglish_to_French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        self.assertIsNotNone(english_to_french)

class TestFrench_to_English(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        self.assertIsNotNone(french_to_english)

unittest.main()