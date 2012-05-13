import Crypto.Random
import Crypto.Random.random
import Crypto.Cipher.XOR

from deckgen.protocol import Protocol

class Deck:
    DEFAULT_CARDS = list(range(52))

    def __init__(self, callback = None, cards = None):
        self._callback = callback
        self.load(cards)
        self.protocol = Protocol(self)

    def __getitem__(self, index):
        return self.cards[index]

    def callback(self):
        if self._callback:
            self._callback()

    def shuffle(self):
        Crypto.Random.random.shuffle(self.cards)

    def load(self, cards):
        if cards:
            self.cards = cards
        else:
            self.cards = list(self.DEFAULT_CARDS)

        for c in range(len(self.cards)):
            if isinstance(self.cards[c], int):
                self.cards[c] = '%02d' % self.cards[c]

    ## Deck generation

    def generateSameKey(self):
        self.sameKey = Crypto.Random.new().read(16)
        #TODO: use a cipher that prevents known-plaintext attacks
        self.sameAlgo = Crypto.Cipher.XOR.new(self.sameKey)

    def getSameKeyEncrypted(self):
        cryptedCards = []
        for card in self.cards:
            cryptedCards.append(self.sameAlgo.encrypt(card))

        return cryptedCards

    def sameKeyDecryptAndLoad(self, cards):
        self.load(cards)
        plainCards = []
        for card in self.cards:
            plainCards.append(self.sameAlgo.decrypt(card))
        self.cards = plainCards

    def generateIndividualKeys(self):
        self.indivKey = []
        self.indivAlgo = []

        for i in range(len(self.cards)):
            self.indivKey.append(Crypto.Random.new().read(16))
            self.indivAlgo.append(Crypto.Cipher.XOR.new(self.indivKey[-1]))

    def getIndividualKeyEncrypted(self):
        cryptedCards = []
        for i in range(len(self.cards)):
            cryptedCards.append(self.indivAlgo[i].encrypt(self.cards[i]))

        return cryptedCards

    ## Generate deck

    def generateDeck(self):
        self.protocol.generateDeck()

    ## Reveal cards

    def revealToMe(self, cards):
        self.protocol.revealToMe(cards)

    def revealToOpponent(self, cards):
        keys = [self.indivKey[i] for i in cards]
        self.protocol.revealToOpponent(cards, keys)

    def revealToBoth(self, cards):
        keys = [self.indivKey[i] for i in cards]
        self.protocol.revealToBoth(cards, keys)

    def verifyDeck(self):
        self.protocol.revealToBoth(list(range(len(self.cards))), self.indivKey)
