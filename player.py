from common import Common
from card_type import *


class Player:
    poker = None

    def __init__(self, name):
        self.name = name
        self.hand_cards = []

    def draw_a_card(self):
        if self.poker is not None:
            self.hand_cards.append(self.poker.distribute())

    def play_cards(self, cards):
        if Common.is_contain_sub_list(self.hand_cards, cards):
            for card in cards:
                self.hand_cards.remove(card)

            return True
        return False

    # 出牌（符合允许的牌型） todo 除单牌，对子的情况
    # 参数：出牌的牌型
    def play_a_type(self, card_type):

        if card_type.name == CardType.CARD_TYPE_SINGLE:
            for card in self.hand_cards:
                if card == card_type.value:
                    self.play_cards(card_type.cards())
                    return True

        elif card_type.name == CardType.CARD_TYPE_DOUBLE:
            doubles = self.find_double()
            for double in doubles:
                if double == card_type.value:
                    self.play_cards(card_type.cards())
                    return True

        return False

    # 能否接牌
    # 参数：目前最后的牌型  todo 除单牌，对子的情况，包括炸弹
    def has_greater_cards(self, card_type):
        if card_type.name == CardType.CARD_TYPE_SINGLE:
            for card in self.hand_cards:
                if card > card_type.value:
                    return True

        elif card_type.name == CardType.CARD_TYPE_DOUBLE:
            doubles = self.find_double()
            for value in doubles:
                if value > card_type.value:
                    return True

        return False

    # 在排序过的手牌中找对子, 返回对子数
    # 逻辑：从第一张开始数，直到倒数第二张，如果点数和后一张不同，过一张，如果和后一张相同，找到对子，过两张
    def find_double(self):
        return Common.find_repeat(self.hand_cards, 2)

    def find_triple(self):
        return Common.find_repeat(self.hand_cards, 3)

    def find_bomb(self):
        return Common.find_repeat(self.hand_cards, 4)

    def analyze(self):
        pass
