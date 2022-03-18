import unittest
from poker import Poker
from player import Player


number = 2

class TestPlayerMethods(unittest.TestCase):

    poker = Poker()

    def test_analysize(self):
        hand_cards = [1, 1, 2, 2, 3, 3, 3, 5, 5, 6, 9, 9, 10, 10, 11, 12, 50, 100]
        hand_cards = [2, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 11, 13]
        hand_cards = [1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 12, 13, 13, 13]



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
