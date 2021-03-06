import unittest
from poker import Poker
from player import Player
from card_type import *


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

    def test_get_next_human(self):

        self.assertIsNone(Poker.get_next_player())

        aidan = Player("Aidan")
        npc1 = Player(Player.NPC_NAME)
        eric = Player("Eric")

        self.poker.add_player(aidan)
        self.poker.add_player(npc1)
        self.poker.add_player(eric)

        # 依次轮
        assert self.poker.get_next_human().name == aidan.name
        assert self.poker.get_next_human().name == eric.name

        # 重复轮
        assert self.poker.get_next_human().name == aidan.name

    def test_distribute_all(self):

        self.poker.shuffle_deck()

        aidan = Player("Aidan")
        computer = Player(Player.NPC_NAME)
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
        # print(aidan.hand_cards)
        # print(computer.hand_cards)
        # print(eric.hand_cards)

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

    def test_analyze_cards_type(self):

        str_cards = "QQAA"
        assert Poker.analyze_card_type(str_cards) == InvalidCardType()

        str_cards = "8"
        assert Poker.analyze_card_type(str_cards) == Single(8)

        str_cards = "55"
        assert Poker.analyze_card_type(str_cards) == Double(5)

        str_cards = "333"
        assert Poker.analyze_card_type(str_cards) == Triple(3)

        str_cards = "6666"
        assert Poker.analyze_card_type(str_cards) == Bomb(6, 4)    # todo 炸弹搭配单牌
        # assert Poker.analyze_card_type(str_cards) == [{'kind': 'bomb'}, {'length': 4}, {'level': 6}]

        str_cards = "J8JJ8"
        assert Poker.analyze_card_type(str_cards) == Combine(11, 8)  # todo 俘虏 对子数据
        # assert Poker.analyze_card_type(str_cards) == [{'kind': 'squad'}, {'length': 5}, {'level': 11}]

        str_cards = "KKAA"
        assert Poker.analyze_card_type(str_cards) == Sister(14, 2)
        # assert Poker.analyze_card_type(str_cards) == [{'kind': 'sister'}, {'length':4}, {'level': 14}]

        str_cards = "A23456789TJQKA"
        assert Poker.analyze_card_type(str_cards) == Rope(14, 14)
        # assert Poker.analyze_card_type(str_cards) == [{'kind': 'string'}, {'length': 14}, {'level': 14}]

    def test_is_continue(self):
        cards = [13, 14]
        assert Poker.is_continue(cards) is True

    def test_analyze_cards(self):

        # 一张牌判断牌型
        cards = [8]
        assert Poker.analyze_card(cards) == Single(8)
        cards = [7]
        assert Poker.analyze_card(cards) != Single(8)

        # 两张牌判断牌型
        cards = [5, 5]
        assert Poker.analyze_card(cards) == Double(5)
        cards = [3, 9]
        assert Poker.analyze_card(cards) == InvalidCardType()

        # 三张牌判断牌型
        cards = [3, 3, 3]
        assert Poker.analyze_card(cards) == Triple(3)
        cards = [2, 3, 4]
        assert Poker.analyze_card(cards) == InvalidCardType()
        cards = [3, 5, 5]
        assert Poker.analyze_card(cards) == InvalidCardType()

        # 四张牌判断牌型
        cards = [13, 13, 14, 14]
        assert Poker.analyze_card(cards) == Sister(14, 2)
        cards = [1, 1, 12, 12]
        assert Poker.analyze_card(cards) == InvalidCardType()
        cards = [5, 6, 7, 8]
        assert Poker.analyze_card(cards) == InvalidCardType()

        #  五张牌判断牌型
        cards = [6, 6, 6, 6, 4]
        assert Poker.analyze_card(cards) == Bomb(6, 4)

        cards = [11, 11, 11, 8, 8]
        assert Poker.analyze_card(cards) == Combine(11, 8)

        cards = [3, 4, 5, 6, 7]
        assert Poker.analyze_card(cards) == Rope(7, 5)

        cards = [3, 4, 5, 6, 8]
        assert Poker.analyze_card(cards) == InvalidCardType()

        # 六张及以上牌型
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        assert Poker.analyze_card(cards) == Rope(14, 14)

        cards = [4, 4, 4, 5, 5, 5, 6, 6, 6]
        assert Poker.analyze_card(cards) == TriSister(6, 3)

        cards = [5, 5, 6, 6, 7, 7, 8, 8]
        assert Poker.analyze_card(cards) == Sister(8, 4)

        cards = [5, 5, 6, 6, 7, 7, 8, 8, 10, 10]
        assert Poker.analyze_card(cards) == InvalidCardType()

        cards = [6, 6, 7, 7, 8, 8]
        assert Poker.analyze_card(cards) == Sister(8, 3)
