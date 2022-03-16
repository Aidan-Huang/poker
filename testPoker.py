import unittest
from poker import Poker

class TestStringMethods(unittest.TestCase):

    def test_is_sister(self):

        poker = Poker()

        # 小于4张牌
        cards = [7, 7]
        self.assertFalse(poker.is_sister(cards))
        cards = [7, 7, 8]
        self.assertFalse(poker.is_sister(cards))

        # 单数牌
        cards = [7, 7, 8, 8, 9]
        self.assertFalse(poker.is_sister(cards))

        # 2姐妹 顺序排列
        cards = [7, 7, 8, 8]
        self.assertTrue(poker.is_sister(cards))
        cards = [8, 8, 7, 7]
        self.assertTrue(poker.is_sister(cards))

        # # 4
        # cards = [7, 8, 7, 9]
        # self.assertFalse(is_sister(cards))


if __name__ == '__main__':
    unittest.main()
