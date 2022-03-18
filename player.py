from common import Common


class Player:
    poker = None

    def __init__(self, name):
        self.name = name
        self.hand_cards = []

        self.single = []
        self.twin = []
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

    def analyze(self):
        pass
