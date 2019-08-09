import random
import decks


class Deck:
    _deck_types = decks.decks
    class DeckError(Exception):
        pass

    def __init__(self, d):
        self.type = d
        self.dealt = []
        if type(d) == str:
            try:
                self.remaining = Deck._deck_types[d]
            except:
                self.remaining = []
        else:
            self.remaining = d

    def _fetch_next(self):
        try:
            a = self.remaining.pop(0)
            self.dealt.append(a)
            return a
        except:
            raise Deck.DeckError("No cards left")

    def draw(self, n=1):
        c = []
        try:
            for i in range(n):
                c.append(self._fetch_next())
            return c
        except:
            raise Deck.DeckError(f"Can't draw {n} cards")

    def put_back(self, card):
        if card in self.dealt:
            self.remaining.append(card)
            self.dealt.remove(self.dealt.index(card))
        else:
            raise Deck.DeckError(f"{card} not in deck")

    def shuffle(self):
        random.shuffle(self.remaining)

    def __len__(self):
        return len(self.remaining)

    def append(self, card):
        self.remaining.append(card)

    def remove(self, card):
        if card in self.remaining:
            self.remaining.remove(self.remaining.index(card))
        else:
            raise Deck.DeckError(f"Can't remove {card} from deck")
