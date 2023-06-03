import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def testf2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def teste2f(self):
        self.assertEqual(english_to_french('Hi'),'Bonjour')

if __name__ == "__main__":
    unittest.main()