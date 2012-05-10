import Crypto.Random
import Crypto.Cipher.XOR

class Deck:
    DEFAULT_CARDS = list(range(52))

    def __init__(self, cards = None):
        if cards:
            self.cards = cards
        else:
            self.cards = self.DEFAULT_CARDS

    def __getitem__(self, index):
        return self.cards[index]

    def generateSameKey(self):
        self.sameKey = Crypto.Random.new().read(16)
        #TODO: use a cipher that prevents known-plaintext attacks
        self.sameAlgo = Crypto.Cipher.XOR.new(self.sameKey)

    def getSameKeyEncrypted(self):
        cryptedCards = []
        for card in self.cards:
            cryptedCards.append(self.sameAlgo.encrypt('%02d' % card))

        return cryptedCards
