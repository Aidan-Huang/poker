from common import Common
from card_type import *


class Player:
    poker = None

    def __init__(self, name):
        self.name = name
        self.hand_cards = []

        self.single = []
        self.double = []
        self.triple = []
        self.bomb = []
        self.three_two = []
        self.sister = []
        self.tri_sister = []
        self.rope = []

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
            if card_type in self.single:
                self.play_cards(card_type.cards)
                self.single.remove(card_type)
                return True

        elif card_type.name == CardType.CARD_TYPE_DOUBLE:
            if card_type in self.double:
                self.play_cards(card_type.cards)
                self.double.remove(card_type)
                return True

        return False

    # 能否接牌
    # 参数：目前最后的牌型  todo 除单牌，对子的情况，包括炸弹
    def has_greater_type(self, card_type):
        if card_type.name == CardType.CARD_TYPE_SINGLE:
            for single in self.single:
                if single.value > card_type.value:
                    return True

        elif card_type.name == CardType.CARD_TYPE_DOUBLE:
            for double in self.double:
                if double.value > card_type.value:
                    return True

        return False

    def find_single(self):

        for card in self.hand_cards:
            single = Single([card])
            self.single.append(single)

        return len(self.hand_cards)

    # 在排序过的手牌中找对子, 返回对子数
    # 逻辑：从第一张开始数，直到倒数第二张，如果点数和后一张不同，过一张，如果和后一张相同，找到对子，过两张
    def find_double(self):

        doubles = Common.find_repeat(self.hand_cards, 2)

        for card in doubles:
            double = Double([card, card])
            self.double.append(double)

        return len(doubles)

    def find_triplet(self):

        triples = Common.find_repeat(self.hand_cards, 3)

        for card in triples:
            triple = Trible([card, card, card])
            self.triple.append(triple)

        return len(triples)

    def find_bomb(self):

        bombs = Common.find_repeat(self.hand_cards, 4)

        for card in bombs:
            bomb = Bomb([card, card, card, card])
            self.bomb.append(bomb)

        return len(bombs)

    def analyze(self):
        pass
