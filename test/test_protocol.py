import unittest

import deckgen.deck
import deckgen.protocol

class TestProtocol(unittest.TestCase):
    def setUp(self):
        self.aliceDeck = deckgen.deck.Deck(self.aliceCallback)
        self.bobDeck = deckgen.deck.Deck(self.bobCallback)

        self.alice = deckgen.protocol.Protocol(self.aliceDeck)
        self.bob   = deckgen.protocol.Protocol(self.bobDeck)

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
