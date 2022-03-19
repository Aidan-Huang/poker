class CardType:
    CARD_TYPE_SINGLE = "single"
    CARD_TYPE_DOUBLE = "double"
    CARD_TYPE_TRIPLE = "triple"
    CARD_TYPE_BOMB = "bomb"

    # 参数：扑克牌数组
    def __init__(self, cards):
        self.name = "ABSTRACT_NAME"
        self.cards = []
        self.value = cards[0]
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
        self.name = CardType.CARD_TYPE_TRIPLE


class Bomb(CardType):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = CardType.CARD_TYPE_TRIPLE


class Sister:
    cards = []
