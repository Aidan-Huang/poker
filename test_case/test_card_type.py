import unittest
from poker import Poker
from player import Player
from card_type import *


class TestCardTypeMethods(unittest.TestCase):

    def test_init_str_cards(self):

        single6 = Single(6)
        assert single6.name == CardType.CARD_TYPE_SINGLE
        assert str(single6) == "single, cards:[6]"

        double3 = Double(3)
        assert double3.name == CardType.CARD_TYPE_DOUBLE
        assert str(double3) == "double, cards:[3, 3]"

        triple7 = Triple(7)
        assert triple7.name == CardType.CARD_TYPE_TRIPLE
        assert str(triple7) == "triple, cards:[7, 7, 7]"

        bomb9 = Bomb(9)
        assert bomb9.name == CardType.CARD_TYPE_BOMB
        # todo 炸弹数据结构调整
        assert str(bomb9) == "bomb, cards:[9, 9, 9, 9]"
        # assert bomb9.is_valid() is False

        rope3_5 = Rope(3, 5)
        assert rope3_5.name == CardType.CARD_TYPE_ROPE
        assert str(rope3_5) == "rope, cards:[3, 4, 5, 6, 7]"

        sister6_3 = Sister(6, 3)
        assert sister6_3.name == CardType.CARD_TYPE_SISTER
        assert str(sister6_3) == "sister, cards:[6, 6, 7, 7, 8, 8]"

        tri_sister4_2 = TriSister(4, 2)
        assert tri_sister4_2.name == CardType.CARD_TYPE_TRI_SISTER
        assert str(tri_sister4_2) == "tri_sister, cards:[4, 4, 4, 5, 5, 5]"


