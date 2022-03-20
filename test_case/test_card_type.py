import unittest
from poker import Poker
from player import Player
from card_type import *


class TestCardTypeMethods(unittest.TestCase):

    def test_init(self):

        single6 = Single(6)
        assert single6.name == CardType.CARD_TYPE_SINGLE

        double3 = Double(3)
        assert double3.name == CardType.CARD_TYPE_DOUBLE

        triple7 = Triple(7)
        assert triple7.name == CardType.CARD_TYPE_TRIPLE

    def test_str(self):

        single6 = Single(6)
        assert str(single6) == "single, cards:[6]"

        double3 = Double(3)
        self.assertEqual(str(double3), "double, cards:[3, 3]")

        triple7 = Triple(7)
        self.assertEqual(str(triple7), "triple, cards:[7, 7, 7]")
