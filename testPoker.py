import unittest
from poker import Poker
from player import Player


class TestPokerMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.poker = Poker()
        Poker.reset_deck()
        Poker.reset_players()

    def test_init(self):
        self.assertEqual(54, len(self.poker.deck))
        # print(self.poker.deck)

    def test_str(self):
        self.assertEqual("Poker: 54 cards", str(self.poker))

    def test_shuffle_deck(self):
        # print(self.poker.deck)
        self.poker.shuffle_deck()
        # print(self.poker.deck)

    def test_get_next_player(self):

        self.assertIsNone(Poker.get_next_player())

        aidan = Player("Aidan")
        eric = Player("Eric")

        self.poker.add_player(aidan)
        self.poker.add_player(eric)

        # 依次轮
        self.assertEqual(aidan.name, self.poker.get_next_player().name)
        self.assertEqual(eric.name, self.poker.get_next_player().name)
        # 重复轮
        self.assertEqual(aidan.name, self.poker.get_next_player().name)

    def test_distribute_all(self):

        self.poker.shuffle_deck()

        aidan = Player("Aidan")
        computer = Player("computer")
        eric = Player("Eric")

        self.poker.add_player(aidan)
        self.poker.add_player(computer)
        self.poker.add_player(eric)

        self.poker.distribute_all()

        self.assertEqual(18, len(aidan.hand_cards))
        self.assertEqual(18, len(computer.hand_cards))
        self.assertEqual(18, len(eric.hand_cards))

        aidan.hand_cards.sort()
        computer.hand_cards.sort()
        eric.hand_cards.sort()
        print(aidan.hand_cards)
        print(computer.hand_cards)
        print(eric.hand_cards)


    def test_is_sister(self):

        # 小于4张牌
        cards = [7, 7]
        self.assertFalse(self.poker.is_sister(cards))
        cards = [7, 7, 8]
        self.assertFalse(self.poker.is_sister(cards))

        # 单数牌
        cards = [7, 7, 8, 8, 9]
        self.assertFalse(self.poker.is_sister(cards))

        # 2姐妹 顺序排列
        cards = [7, 7, 8, 8]
        self.assertTrue(self.poker.is_sister(cards))
        cards = [8, 8, 7, 7]
        self.assertTrue(self.poker.is_sister(cards))

        # # 4
        # cards = [7, 8, 7, 9]
        # self.assertFalse(is_sister(cards))


if __name__ == '__main__':
    unittest.main()
