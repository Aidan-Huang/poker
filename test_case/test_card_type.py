import unittest
from poker import Poker
from player import Player
from card_type import *


class TestCardTypeMethods(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_init(self):

        card_6 = Single([6])
        self.assertEqual(card_6.name, CardType.CARD_TYPE_SINGLE)

    def test_str(self):
        single_6 = Single([6])
        self.assertEqual(str(single_6), "single, cards:[6]")

        double_4 = Double([4, 4])
        self.assertEqual(str(double_4), "double, cards:[4, 4]")

    def test_test(self):

        class HandCards:
            def __init__(self, cards):
                self.cards = cards
                # for card in cards:
                #     self.cards.append(card)

        three_cards = [1, 2, 3]

        hand_cards = HandCards(three_cards)

        three_cards = [4, 5, 6]

        # print(hand_cards.cards)


if __name__ == '__main__':
    unittest.main()
