from common import Common
from player import Player
from eric_poker import *
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

    @staticmethod
    def analyze_card_type(str_cards):
        return identify_your_card(str_cards)

    @staticmethod
    # 是否连续
    def is_continue(cards):
        for i in range(len(cards) - 1):
            if cards[i + 1] != cards[i] + 1:
                return False
        return True

    @staticmethod
    # 是否绳子
    def is_rope(cards):
        if len(cards) < 5:
            return False

        double_card = Common.find_repeat(cards, 2)
        if len(double_card) == 0:
            if Poker.is_continue(cards):
                return True

        return False

    @staticmethod
    def analyze_card(cards):
        if not cards:
            return InvalidCardType()

        n = len(cards)

        cards.sort()

        # 五张牌及以上，先判是否绳子
        if n > 4:
            if Poker.is_rope(cards):
                return Rope(cards[-1], n)

        first_card = cards[0]

        bomb_card = Common.find_repeat(cards, 4)
        triple_card = Common.find_repeat(cards, 3)
        double_card = Common.find_repeat(cards, 2)

        remove_repeat = Common.remove_repeat(cards)

        # 单牌
        if n == 1:
            return Single(first_card)
        # 两张牌 判断是否对子
        elif n == 2:
            if cards[0] == cards[1]:
                return Double(first_card)
            else:
                return InvalidCardType()
        # 三张牌 判断是否三张一致
        elif n == 3:
            triple_card = Common.find_repeat(cards, 3)
            if len(triple_card) == 1:
                return Triple(first_card)
            else:
                return InvalidCardType()

        # 四张牌，判断是否姐妹，连续两对是姐妹 todo A 处理
        elif n == 4:
            if len(double_card) == 2:
                if Poker.is_continue(double_card):
                    return Sister(cards[2], 2)

            return InvalidCardType()

        # 五张牌，判断是否俘虏或炸弹
        elif n == 5:
            # 炸弹
            if len(bomb_card) == 1:
                for card in remove_repeat:
                    if card in bomb_card:
                        remove_repeat.remove(card)
                return Bomb(bomb_card[0], remove_repeat[0])
            # 俘虏
            elif len(triple_card) == 1 and len(double_card) == 2:
                for card in remove_repeat:
                    if card in triple_card:
                        remove_repeat.remove(card)
                return Combine(triple_card[0], remove_repeat[0])

            return InvalidCardType()

        # 六张及以上牌型， 判断是否是绳子，姐妹或三姐妹
        else:
            if n % 3 == 0:
                if len(triple_card) == n / 3:
                    triple_card.sort()
                    if Poker.is_continue(triple_card):
                        return TriSister(triple_card[-1], n / 3)

            elif n % 2 == 0:
                if len(double_card) == n / 2:
                    double_card.sort()
                    if Poker.is_continue(double_card):
                        return Sister(double_card[-1], n /2)

            return InvalidCardType()


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
