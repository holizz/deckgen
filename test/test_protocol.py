import unittest

from deckgen.deck import Deck
from deckgen.protocol import Protocol

class TestProtocol(unittest.TestCase):
    def setUp(self):
        self.aliceDeck = Deck(self.aliceCallback)
        self.bobDeck = Deck(self.bobCallback)

        self.alice = Protocol(self.aliceDeck)
        self.bob   = Protocol(self.bobDeck)

        self.alice.output = self.bob.input
        self.bob.output   = self.alice.input

    def aliceCallback(self):
        self.assertEqual(len(self.aliceDeck.cards), 52)
        self.aliceCallbackCalled = True
    def bobCallback(self):
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
