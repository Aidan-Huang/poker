import unittest
from poker import Poker


class TestStringMethods(unittest.TestCase):

    poker = Poker()

    def test_init(self):
        self.assertEqual(54, len(self.poker.deck))
        print(self.poker.deck)

    def test_str(self):
        self.assertEqual("Poker: 54 cards", str(self.poker))

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
