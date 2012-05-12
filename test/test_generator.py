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
        self.assertEqual(len(self.aliceDeck.cards), 52)
        self.aliceCallbackCalled = True
    def bobCallback(self, deck):
        self.bobDeck = deck
        self.assertEqual(len(self.bobDeck.cards), 52)
        self.bobCallbackCalled = True

    def testGenerateDeck(self):
        self.aliceCallbackCalled = False
        self.bobCallbackCalled = False

        self.alice.generateDeck()

        self.assertTrue(self.aliceCallbackCalled, 'Expected alice-callback to be called')
        self.assertTrue(self.bobCallbackCalled, 'Expected bob-callback to be called')

if __name__ == '__main__':
    unittest.main()
