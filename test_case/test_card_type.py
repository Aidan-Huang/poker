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

        bomb9 = Bomb(9, 3)
        assert bomb9.name == CardType.CARD_TYPE_BOMB
        assert str(bomb9) == "bomb, cards:[9, 9, 9, 9, 3]"

        rope7_5 = Rope(7, 5)
        assert rope7_5.name == CardType.CARD_TYPE_ROPE
        assert str(rope7_5) == "rope, cards:[3, 4, 5, 6, 7]"

        sister8_3 = Sister(8, 3)
        assert sister8_3.name == CardType.CARD_TYPE_SISTER
        assert str(sister8_3) == "sister, cards:[6, 6, 7, 7, 8, 8]"

        tri_sister5_2 = TriSister(5, 2)
        assert tri_sister5_2.name == CardType.CARD_TYPE_TRI_SISTER
        assert str(tri_sister5_2) == "tri_sister, cards:[4, 4, 4, 5, 5, 5]"

        combine5_7 = Combine(5, 7)
        assert combine5_7.name == CardType.CARD_TYPE_COMBINE
        assert str(combine5_7) == "combine, cards:[5, 5, 5, 7, 7]"




