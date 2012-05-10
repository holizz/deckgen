import Crypto.Random

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
        self.sameAlgo = someCipherOrAnother

    def getSameKeyEncrypted(self):
        self.sameCryptedCards = []
        for card in self.cards:
            doSomething()
