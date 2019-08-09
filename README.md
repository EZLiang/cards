# cards

## How_to_use

### Deck_class

 * Initialization: <br />
 Takes 1 argument: `Deck(builtin deck name or list of cards)`. See [Adding decks](#Adding_decks).
 * `Deck.draw(n=1)`: <br />
 Takes 1 argument, `n`, how many cards to draw (default is 1), and returns them as a list. If it can't draw `n` cards, it throws a [`Deck.DeckError`](#`Deck.DeckError(*args)`_class).
 * `Deck.put_back(card)`: <br />
 Puts `card` back in the deck if possible, else throws a [`Deck.DeckError`](#`Deck.DeckError(*args)`)_class.
 * `Deck.shuffle()`: <br />
 No arguments, shuffles the deck.
 * `Deck.append(card)`: <br />
 Adds `card` to the bottom of the deck.
 * `Deck.remove(card)`: <br />
 Removes `card` if possible, else throws a [`Deck.DeckError`](#`Deck.DeckError(*args)`_class).
 * `len(Deck)`: <br />
 Returns how many cards are in the deck.

#### `Deck.DeckError(*args)`_class

An error class for things that go wrong in manipulating decks.
### Hand_class

 * Initialization: <br />
 Takes no arguments.
 * `Hand.pick_up(card)`: <br />
 Adds `card` to the hand.
 * `Hand.put_down(card)`: <br />
 Removes `card` from the hand if it can, otherwise throws a [`Hand.HandError`](#`Hand.HandError(*args)`_class).
 * `Hand.draw(d)`: <br />
 Draws a card from [Deck](#Deck_class) d or throws [`Deck.DeckError`](#`Deck.DeckError(*args)`_class).
 * `Hand.ret(d, card)`: <br />
 Transfers `card` from the hand to [Deck](#Deck_class) d else throws error.

#### `Hand.HandError(*args)`_class
An error class for things that go wrong in manipulating decks.

## Adding_decks
If you want to add decks to this repo, please start a pull request.
