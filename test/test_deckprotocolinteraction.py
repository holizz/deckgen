import unittest

import mock

from deckgen.deck import Deck
from deckgen.protocol import Protocol

class TestDeckProtocolInteraction(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def testGenerateDeck(self):
        with mock.patch.object(Protocol, 'generateDeck') as mockMethod:
            self.deck.generateDeck()
            mockMethod.assertCalledOnce()

if __name__ == '__main__':
    unittest.main()
