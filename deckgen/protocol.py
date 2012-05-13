class Protocol:
    def __init__(self, deck):
        self.deck = deck
        self.output = None
        self.state = 'WAIT'

    def input(self, data):
        if self.state == 'WAIT' and data['action'] == 'NEWDECK':
            self.deck.load(data['deck'])
            #  5. Bob picks an encryption key B and uses this to encrypt each card of the encrypted and shuffled deck.
            self.deck.generateSameKey()
            #  6. Bob shuffles the deck.
            self.deck.shuffle()
            #  7. Bob passes the double encrypted and shuffled deck back to Alice.
            self.state = 'WAIT-AFTER-SAMECRYPTEDDECK'
            self.output({'action': 'SAMECRYPTEDDECK', 'deck': self.deck.getSameKeyEncrypted()})

        elif self.state == 'WAIT-AFTER-NEWDECK' and data['action'] == 'SAMECRYPTEDDECK':
            #  8. Alice decrypts each card using her key A. This still leaves Bob's encryption in place though so she cannot know which card is which.
            self.deck.sameKeyDecryptAndLoad(data['deck'])
            #  9. Alice picks one encryption key for each card (A1, A2, etc.) and encrypts them individually.
            self.deck.generateIndividualKeys()
            # 10. Alice passes the deck to Bob.
            self.state = 'WAIT-AFTER-INDIVIDUALLYCRYPTEDDECK'
            self.output({'action': 'INDIVIDUALLYCRYPTEDDECK', 'deck': self.deck.getIndividualKeyEncrypted()})

        elif self.state == 'WAIT-AFTER-SAMECRYPTEDDECK' and data['action'] == 'INDIVIDUALLYCRYPTEDDECK':
            # 11. Bob decrypts each card using his key B. This still leaves Alice's individual encryption in place though so he cannot know which card is which.
            self.deck.sameKeyDecryptAndLoad(data['deck'])
            # 12. Bob picks one encryption key for each card (B1, B2, etc.) and encrypts them individually.
            self.deck.generateIndividualKeys()
            # 13. Bob passes the deck back to Alice.
            self.state = 'WAIT-AFTER-FINALDECK'
            self.output({'action': 'FINALDECK', 'deck': self.deck.getIndividualKeyEncrypted()})

            self.deck.callback()

        elif self.state == 'WAIT-AFTER-INDIVIDUALLYCRYPTEDDECK' and data['action'] == 'FINALDECK':
            # 14. Alice publishes the deck for everyone playing (in this case only Alice and Bob, see below on expansion though).
            self.deck.load(data['deck'])

            self.state = 'WAIT-AFTER-FINALDECK'

            self.deck.callback()

        else:
            raise NotImplementedError('state: %s, action: %s' % (self.state, data['action']))

    def generateDeck(self):
        #  1. Alice and Bob agree on a certain "deck" of cards. In practice, this means they agree on a set of numbers or other data such that each element of the set represents a card.
        #  2. Alice picks an encryption key A and uses this to encrypt each card of the deck.
        self.deck.generateSameKey()
        #  3. Alice shuffles the cards.
        self.deck.shuffle()
        #  4. Alice passes the encrypted and shuffled deck to Bob. With the encryption in place, Bob cannot know which card is which.
        self.state = 'WAIT-AFTER-NEWDECK'
        self.output({'action': 'NEWDECK', 'deck': self.deck.getSameKeyEncrypted()})

    def revealToMe(self, card):
        pass

    def revealToOpponent(self, card, key):
        pass

    def revealToBoth(self, card, key):
        pass
