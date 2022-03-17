class single:
    card = -1


class double:
    cards = [-1, -1]


class trible:
    cards = [-1, -1, -1]


class sister:
    cards = []


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


"""
定义扑克类
"""


class Poker(metaclass=Singleton):
    BLACK_JOKER = 50
    RED_JOKER = 100

    cards_num = 54
    deck = []

    def __init__(self):

        for suit in range(4):
            for i in range(13):
                self.deck.append(i + 1)

        self.deck.append(Poker.BLACK_JOKER)
        self.deck.append(Poker.RED_JOKER)

    def __str__(self) -> str:
        return f"Poker: {self.cards_num} cards"

    def is_sister(self, cards):
        if len(cards) < 4:
            return False
        elif len(cards) % 2 != 0:
            return False
        return True
