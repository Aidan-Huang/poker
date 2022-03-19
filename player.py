from common import Common
from card_type import *


class Player:
    poker = None

    def __init__(self, name):
        self.name = name
        self.hand_cards = []

        self.single = []
        self.double = []
        self.triplet = []
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

    def analyze(self):
        pass
