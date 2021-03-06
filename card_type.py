
class CardType:
    CARD_TYPE_SINGLE = "single"
    CARD_TYPE_DOUBLE = "double"
    CARD_TYPE_TRIPLE = "triple"
    CARD_TYPE_ROPE = "rope"
    CARD_TYPE_SISTER = "sister"
    CARD_TYPE_TRI_SISTER = "tri_sister"
    CARD_TYPE_BOMB = "bomb"
    CARD_TYPE_COMBINE = "combine"
    CARD_TYPE_INVALID_TYPE = "invalid_type"

    # 参数：扑克牌数组
    def __init__(self, card):
        self.name = "ABSTRACT_TYPE"
        self.length = 1
        self.value = card
        self.other_value = 0

    def __str__(self):
        return f"{self.name}, cards:{self.cards()}"

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def __gt__(self, other):
        return self.name == other.name and self.value > other.value

    def cards(self):
        return_cards = []
        for _ in range(self.length):
            return_cards.append(self.value)

        return return_cards


class InvalidCardType(CardType):

    def __init__(self):
        self.name = CardType.CARD_TYPE_INVALID_TYPE
        self.value = None


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

    def __init__(self, card, other_card):
        super().__init__(card)
        self.name = CardType.CARD_TYPE_BOMB
        self.length = 5
        self.other_value = other_card

    def __gt__(self, other):
        if self.name == other.name:
            return self.value > other.value
        return True

    def cards(self):
        cards = super().cards()
        cards[self.length - 1] = self.other_value
        return cards

    # def is_valid(self):
    #     return self.cards()[self.length - 1] != self.value


class Rope(CardType):

    def __init__(self, card, length):
        super().__init__(card)
        self.name = CardType.CARD_TYPE_ROPE
        self.length = length
        self.min_limit = 5
        self.repeat = 1

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value and self.length == other.length

    def cards(self):
        return_cards = []
        for i in range(self.length):
            for j in range(self.repeat):
                return_cards.append(self.value - self.length + i + 1)
        return return_cards


class Sister(Rope):

    def __init__(self, card, length):
        super().__init__(card, length)
        self.name = CardType.CARD_TYPE_SISTER
        self.min_limit = 2
        self.repeat = 2


class TriSister(Sister):

    def __init__(self, card, length):
        super().__init__(card, length)
        self.name = CardType.CARD_TYPE_TRI_SISTER
        self.repeat = 3


class Combine(CardType):

    def __init__(self, triple, double):
        self.name = CardType.CARD_TYPE_COMBINE
        self.value = triple
        self.other_value = double
        self.length = 5

    def cards(self):
        return_cards = []
        for _ in range(3):
            return_cards.append(self.value)

        for _ in range(2):
            return_cards.append(self.other_value)

        return return_cards
