from typing import List


class CardType:
    CARD_TYPE_SINGLE = "single"
    CARD_TYPE_DOUBLE = "double"
    CARD_TYPE_TRIPLE = "triple"
    CARD_TYPE_BOMB = "bomb"
    CARD_TYPE_ROPE = "rope"
    CARD_TYPE_SISTER = "sister"
    CARD_TYPE_TRI_SISTER = "tri_sister"

    # 参数：扑克牌数组
    def __init__(self, card):
        self.name = "ABSTRACT_TYPE"
        self.length = 1
        self.value = card

    def __str__(self):
        return f"{self.name}, cards:{self.Cards()}"

    def Cards(self):
        cards = []
        for _ in range(self.length):
            cards.append(self.value)

        return cards


class Single(CardType):

    def __init__(self, card):
        super().__init__(card)
        self.name = CardType.CARD_TYPE_SINGLE
        self.length = 1


class Double(CardType):

    def __init__(self, card):
        super().__init__(card)
        self.name = CardType.CARD_TYPE_DOUBLE
        self.length = 2


class Triple(CardType):

    def __init__(self, card):
        super().__init__(card)
        self.name = CardType.CARD_TYPE_TRIPLE
        self.length = 3


class Bomb(CardType):

    def __init__(self, cards):
        super().__init__(cards)
        self.name = CardType.CARD_TYPE_BOMB
        self.length = 5
