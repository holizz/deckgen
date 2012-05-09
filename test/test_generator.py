import unittest

import deckgen.generator

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.alice = deckgen.generator.Generator(self.aliceCallback)
        self.bob   = deckgen.generator.Generator(self.bobCallback)

        self.alice.output = self.bob.input
        self.bob.output   = self.alice.input

    def aliceCallback(self, deck):
        self.aliceDeck = deck
    def bobCallback(self, deck):
        self.bobDeck = deck

    def _testGenerateDeck(self):
        self.assertEqual(self.aliceDeck, [])
        self.assertEqual(self.bobDeck, [])
        self.callbackCalled = True
    def testGenerateDeck(self):
        self.callbackCalled = False
        self.alice.generateDeck(self._testGenerateDeck)
        self.assertTrue(self.callbackCalled, 'Expected callback to be called')

if __name__ == '__main__':
    unittest.main()
