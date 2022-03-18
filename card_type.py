class CardType:
    CARD_TYPE_SINGLE = "single"
    CARD_TYPE_DOUBLE = "double"
    CARD_TYPE_TRIPLET = "triplet"

    def __init__(self, cards):
        self.name = "ABSTRACT_NAME"
        self.cards = []
        for card in cards:
            self.cards.append(card)


    def __str__(self):
        return f"{self.name}, cards:{self.cards}"


class Single(CardType):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = CardType.CARD_TYPE_SINGLE


class Double(CardType):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = CardType.CARD_TYPE_DOUBLE


class Trible(CardType):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = CardType.CARD_TYPE_TRIPLET

class Sister:
    cards = []
