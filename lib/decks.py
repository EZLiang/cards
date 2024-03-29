class DeckSample:
    normal = [
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"
    ]
    poker = [
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "joker", "Joker"
    ]
    number = [
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H",
        "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S"
    ]
    pure_number = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

decks = {
    "normal": DeckSample.normal,
    "poker": DeckSample.poker,
    "number": DeckSample.number,
    "purenumber": DeckSample.pure_number
}
