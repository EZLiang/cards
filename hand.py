import deck

class Hand:
    class HandError(Exception):
        pass

    def __init__(self):
        self.cards = []
        pass

    def __len__(self):
        return len(self.cards)

    def pick_up(self, card):
        self.cards.append(card)

    def put_down(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise Hand.HandError(f"{card} not in hand")

    def draw(self, d: deck.Deck):
        self.pick_up(d.draw())

    def ret(self, d: deck.Deck, card):
        self.put_down(card)
        d.put_back(card)
