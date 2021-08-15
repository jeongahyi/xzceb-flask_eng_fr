import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertNotEqual(english_to_french(""), "Bonjour")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def testFrenchToEnglish(self):
        self.assertNotEqual(french_to_english(""), "Hello")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()