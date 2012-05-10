import unittest

from deckgen.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.sampleCards = [
                21, 34, 22, 20, 23, 49, 15, 19, 17, 37, 32, 14,  2,
                27, 24, 29, 12, 31, 33, 48, 50, 39, 36, 40, 10, 38,
                45, 25,  1, 47, 18,  3, 16, 26, 28, 13,  4,  0,  8,
                43, 51, 35,  7, 30, 11,  9, 42,  5, 41, 44, 46,  6,
                ]

    def testDefaultInstantiation(self):
        deck = Deck()
        self.assertEqual(deck.cards, list(range(0,52)))
        self.assertEqual(deck[0], 0)
        self.assertEqual(deck[51], 51)

    def testInstantiation(self):
        deck = Deck(self.sampleCards)
        self.assertEqual(deck.cards, self.sampleCards)
        self.assertEqual(deck[0], 21)
        self.assertEqual(deck[51], 6)

    def testGenerateSameKey(self):
        deck = Deck()
        deck.generateSameKey()
        print(repr(deck.sameKey))
        self.assertTrue(isinstance(deck.sameKey, str))

    def testGenerateSameKey(self):
        deck = Deck()
        deck.generateSameKey()
        cryptedCards = deck.getSameKeyEncrypted()
        print(cryptedCards)
        self.assertNotEqual(cryptedCards[0], 0)

    # def testLoading(self):
    #     deck.load(data['deck'])

    # def testShuffle(self):
    #     deck.shuffle()

        # deck.generateSameKey()
        # deck.getSameKeyEncrypted()
        # deck.sameKeyDecryptAndLoad(data['deck'])
        # deck.generateIndividualKeys()
        # deck.getIndividualKeyEncrypted()
        # deck.sameKeyDecryptAndLoad(data['deck'])
        # deck.generateIndividualKeys()
        # deck.getIndividualKeyEncrypted()

if __name__ == '__main__':
    unittest.main()
