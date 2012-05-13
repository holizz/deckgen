import unittest

from deckgen.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.defaultCards = ['%02d' % x for x in list(range(52))]
        self.sampleCards = [
                21, 34, 22, 20, 23, 49, 15, 19, 17, 37, 32, 14,  2,
                27, 24, 29, 12, 31, 33, 48, 50, 39, 36, 40, 10, 38,
                45, 25,  1, 47, 18,  3, 16, 26, 28, 13,  4,  0,  8,
                43, 51, 35,  7, 30, 11,  9, 42,  5, 41, 44, 46,  6,
                ]
        self.deck = Deck()

    def testDefaultInstantiation(self):
        self.assertEqual(self.deck.cards, self.defaultCards)
        self.assertEqual(self.deck[0], '00')
        self.assertEqual(self.deck[51], '51')

    def testInstantiation(self):
        self.deck = Deck(None, self.sampleCards)
        self.assertEqual(self.deck.cards, self.sampleCards)
        self.assertEqual(self.deck[0], '21')
        self.assertEqual(self.deck[51], '06')

    def testGenerateSameKey(self):
        self.deck.generateSameKey()
        self.assertTrue(isinstance(self.deck.sameKey, str))

    def testGenerateSameKey(self):
        self.deck.generateSameKey()
        cryptedCards = self.deck.getSameKeyEncrypted()
        self.assertNotEqual(cryptedCards[0], '00')

    def testShuffle(self):
        self.deck.shuffle()
        # This test will be correct most of the time
        self.assertNotEqual(self.deck.cards, self.defaultCards)

    def testLoad(self):
        self.deck.load(self.sampleCards)
        self.assertEqual(self.deck.cards, self.sampleCards)
        self.assertEqual(self.deck[0], '21')

    def testSameKeyDecryptAndLoad(self):
        self.deck.generateSameKey()
        cards = ['xxy', 'xyz', 'xxx']
        self.deck.sameKeyDecryptAndLoad(cards)
        self.assertNotEqual(self.deck.cards, cards)
        self.assertNotEqual(self.deck[0], 'xxy')

    def testGenerateIndividualKeys(self):
        self.deck.generateIndividualKeys()
        crypted = self.deck.getIndividualKeyEncrypted()
        self.assertNotEqual(crypted[0], '00')

if __name__ == '__main__':
    unittest.main()
