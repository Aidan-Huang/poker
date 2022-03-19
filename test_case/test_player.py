import unittest
from poker import Poker
from player import Player
from card_type import *


class TestPlayerMethods(unittest.TestCase):
    poker = Poker()

    # 分析手牌 todo
    def test_analysize(self):
        hand_cards = [1, 1, 2, 2, 3, 3, 3, 5, 5, 6, 9, 9, 10, 10, 11, 12, 50, 100]
        hand_cards = [2, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 11, 13]
        hand_cards = [1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 12, 13, 13, 13]

    def test_play_cards(self):
        aidan = Player("Aidan")
        self.poker.add_player(aidan)

        hand_cards = [1, 1, 2, 2, 3]

        aidan.hand_cards = hand_cards;

        self.assertTrue(aidan.play_cards([2, 2]))

        self.assertEqual([1, 1, 3], aidan.hand_cards)

        self.assertFalse(aidan.play_cards([2, 2]))

        self.assertEqual([1, 1, 3], aidan.hand_cards)

        self.assertTrue(aidan.play_cards([3]))

        self.assertEqual([1, 1], aidan.hand_cards)

    def test_play_a_type(self):
        aidan = Player("Aidan")
        self.poker.add_player(aidan)

        hand_cards = [1, 1, 2, 2, 3]

        aidan.hand_cards = hand_cards

        double1 = Double([1, 1])
        double2 = Double([2, 2])
        double3 = Double([3, 3])
        single3 = Single([3])

        aidan.single.append(single3)
        aidan.double.append(double2)
        aidan.double.append(double1)

        assert aidan.play_a_type(double2) is True
        assert aidan.play_a_type(double3) is False

        assert len(aidan.hand_cards) == 3
        assert len(aidan.double) == 1

        assert aidan.play_a_type(single3) is True

        assert len(aidan.hand_cards) == 2
        assert len(aidan.single) == 0


    def test_draw_a_card(self):
        deck = [8, 2, 1, 3]
        Poker.deck = deck

        aidan = Player("Aidan")
        eric = Player("Eric")

        self.poker.add_player(aidan)
        self.poker.add_player(eric)

        aidan.draw_a_card()
        eric.draw_a_card()
        aidan.draw_a_card()

        self.assertEqual(2, len(aidan.hand_cards))
        self.assertEqual(1, len(eric.hand_cards))

        self.assertEqual(3, aidan.hand_cards[0])
        self.assertEqual(1, eric.hand_cards[0])
        self.assertEqual(2, aidan.hand_cards[1])


if __name__ == '__main__':
    unittest.main()
