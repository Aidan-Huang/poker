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

    def test_find_double(self):
        aidan = Player("Aidan")
        self.poker.add_player(aidan)

        hand_cards = [1, 1, 1, 2, 2, 2, 2, 3, 7, 7]

        aidan.hand_cards = hand_cards

        assert aidan.find_double() == 4
        assert len(aidan.double) == 4

    def test_has_greater_type(self):

        aidan = Player("Aidan")
        eric = Player("Eric")
        aidan_hand_cards = [4, 4, 10, 10, 6]
        aidan.hand_cards = aidan_hand_cards
        double4 = Double([4, 4])
        double10 = Double([10, 10])
        single6 = Single([6])
        aidan.double.append(double4)
        aidan.double.append(double10)
        aidan.single.append(single6)

        eric_hand_cards = [3, 3, 5, 5, 10]
        eric.hand_cards = eric_hand_cards
        double3 = Double([3, 3])
        double5 = Double([5, 5])
        single10 = Single([10])
        eric.double.append(double3)
        eric.double.append(double5)
        eric.single.append(single10)

        self.poker.add_player(aidan)
        self.poker.add_player(eric)

        single7 = Single([7])
        double7 = Double([7, 7])

        assert aidan.has_greater_type(single7) is False
        assert eric.has_greater_type(single7) is True
        assert aidan.has_greater_type(double7) is True
        assert eric.has_greater_type(double7) is False



if __name__ == '__main__':
    unittest.main()
