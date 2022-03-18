from player import Player
import random

# 引入单例模型

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

    current_player_index = -1
    players = []

    def __init__(self):
        Poker.reset_deck()

    @staticmethod
    def reset_deck():
        Poker.deck.clear()

        for suit in range(4):
            for i in range(13):
                Poker.deck.append(i + 1)

        Poker.deck.append(Poker.BLACK_JOKER)
        Poker.deck.append(Poker.RED_JOKER)

    @staticmethod
    def reset_players():
        Poker.current_player_index = -1
        Poker.players.clear()

    def __str__(self) -> str:
        return f"Poker: {self.cards_num} cards"



    def add_player(self, player):
        self.players.append(player)
        player.poker = self

    def shuffle_deck(self):
        random.shuffle(Poker.deck)

    def distribute(self):
        return Poker.deck.pop()

    @staticmethod
    def distribute_all():
        if len(Poker.players) > 0:
            while len(Poker.deck) > 0:
                Poker.get_next_player().draw_a_card()


    @staticmethod
    def get_next_player():
        if len(Poker.players) < 1:
            return None
        else:
            Poker.current_player_index = (Poker.current_player_index + 1) % len(Poker.players)
            return Poker.players[Poker.current_player_index]



    @staticmethod
    def check_cards_if_has(who, whatcard):

        for card in who:
            if card == whatcard:
                who.remove(whatcard)

    def is_sister(self, cards):
        if len(cards) < 4:
            return False
        elif len(cards) % 2 != 0:
            return False
        return True
