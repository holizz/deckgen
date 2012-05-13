import unittest

import mock

from deckgen.deck import Deck
from deckgen.protocol import Protocol

class TestDeckProtocolInteraction(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.deck.indivKey = ['k%02d' % n for n in range(52)]

    def testGenerateDeck(self):
        with mock.patch.object(Protocol, 'generateDeck') as mockMethod:
            self.deck.generateDeck()
            mockMethod.assert_called_once()

    def testRevealToMe(self):
        with mock.patch.object(Protocol, 'revealToMe') as mockMethod:
            self.deck.revealToMe([15])
            mockMethod.assert_called_once_with([15])

    def testRevealToOpponent(self):
        with mock.patch.object(Protocol, 'revealToOpponent') as mockMethod:
            self.deck.revealToOpponent([2, 3])
            mockMethod.assert_called_once_with([2, 3], [self.deck.indivKey[2], self.deck.indivKey[3]])

    def testRevealToBoth(self):
        with mock.patch.object(Protocol, 'revealToBoth') as mockMethod:
            self.deck.revealToBoth([1])
            mockMethod.assert_called_once_with([1], [self.deck.indivKey[1]])

    def testVerifyDeck(self):
        with mock.patch.object(Protocol, 'revealToBoth') as mockMethod:
            self.deck.verifyDeck()
            mockMethod.assert_called_once_with(list(range(52)), self.deck.indivKey)

if __name__ == '__main__':
    unittest.main()
