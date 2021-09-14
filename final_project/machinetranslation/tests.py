import unittest

from translator import english_to_french, french_to_english

class TestTranslates(unittest.TestCase):
    def testNotNullFrenchToEnglish(self):
        self.assertNotEqual(english_to_french("Hello"),'')

    def testNotNullEnglishToFrench(self):
        self.assertNotEqual(french_to_english("Bonjour"),'')

    def testFrenchToEnglish(self):
        self.assertEqual(english_to_french("Hello"),'Bonjour')
        
    def testEnglishToFrench(self):
        self.assertEqual(french_to_english("Bonjour"),'Hello')

unittest.main()