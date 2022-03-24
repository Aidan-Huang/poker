import random
import unittest
from card_type import *

# from testcase import TestPokerMethods

is_on = True
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 100]
user1_card = []
user2_card = []
user3_card = []


def deal_a_card(who):
    a = random.randint(0, len(cards) - 1)
    new_card = cards[a]
    who.append(new_card)
    cards.remove(new_card)


def deal_cards():
    for a in range(18):
        if not len(cards) == 0:
            deal_a_card(user1_card)
            deal_a_card(user2_card)
            deal_a_card(user3_card)
    user1_card.sort(reverse=True)
    user2_card.sort(reverse=True)
    user3_card.sort(reverse=True)


def show_ones_cards(who):
    a = who
    b = 0
    for x in who:
        if x == 100:
            a.insert(b, "P")
            a.remove(100)
        if x == 50:
            a.insert(b, "R")
            a.remove(50)
        if x == 13:
            a.insert(b, "K")
            a.remove(13)
        if x == 12:
            a.insert(b, "Q")
            a.remove(12)
        if x == 11:
            a.insert(b, "J")
            a.remove(11)
        if x == 1:
            a.insert(b, "A")
            a.remove(1)
        if x == 10:
            a.insert(b, "T")
            a.remove(10)
        b += 1


def show_cards():
    show_ones_cards(user1_card)
    show_ones_cards(user2_card)
    show_ones_cards(user3_card)


def is_string(what):
    string = False
    what.sort(reverse=True)
    length = len(what)
    if length >= 5:
        b = 0
        for a in range(length - 1):
            if int(what[b]) == int(what[b + 1]) + 1:
                string = True
            else:
                string = False
                break
            b += 1
    return string


def is_onecard(what):
    onecard = False
    length = len(what)
    if length == 1:
        onecard = True
    else:
        onecard = False
    return onecard


def is_twocard(what):
    twocard = False
    length = len(what)
    if length == 2 and what[0] == what[1]:
        twocard = True
    else:
        twocard = False
    return twocard


def is_threecard(what):
    threecard = False
    length = len(what)
    if length == 3 and what[0] == what[1] == what[2]:
        threecard = True
    else:
        threecard = False
    return threecard


def is_squad(what):
    squad = False
    length = len(what)
    what.sort(reverse=True)
    if length == 5 and what[0] == what[1] == what[2] and what[3] == what[4]:
        squad = True
    elif length == 5 and what[2] == what[3] == what[4] and what[0] == what[1]:
        squad = True
    else:
        squad = False
    return squad


def is_bomb(what):
    bomb = False
    length = len(what)
    if length == 4 and what[0] == what[1] == what[2] == what[3]:
        bomb = True
    else:
        bomb = False
    return bomb


def is_sister(what):
    length = len(what)
    if length % 2 != 0:
        return False
    if length < 4:
        return False
    what.sort(reverse=True)
    index = 0
    for a in range(int(length / 2) - 1):
        if what[index] != what[index + 1]:
            return False
        if what[index] != what[index + 2] + 1:
            return False
        index += 2
    return True


def identify_your_card(ti):
    true_use_card = []
    for a in ti:
        true_use_card.append(a)
    b = 0
    # print(true_use_card)
    for x in true_use_card:
        if x == "P":
            true_use_card.insert(b, 100)
            true_use_card.remove("P")
        if x == "R":
            true_use_card.insert(b, 50)
            true_use_card.remove(50)
        if x == "K":
            true_use_card.insert(b, 13)
            true_use_card.remove("K")
        if x == "Q":
            true_use_card.insert(b, 12)
            true_use_card.remove("Q")
        if x == "J":
            true_use_card.insert(b, 11)
            true_use_card.remove("J")
        if x == "A":
            true_use_card.insert(b, 14)
            true_use_card.remove("A")
        if x == "T":
            true_use_card.insert(b, 10)
            true_use_card.remove("T")
        b += 1
    true_use_card1 = []
    for y in true_use_card:
        true_use_card1.append(int(y))
    true_use_card = true_use_card1
    true_use_card.sort(reverse=True)
    num = 0
    for b in true_use_card:
        if b == 14:
            num += 1
    true_use_card.sort(reverse=True)
    while num != -1:
        if_string = is_string(true_use_card)
        if_onecard = is_onecard(true_use_card)
        if_twocard = is_twocard(true_use_card)
        if_threecard = is_threecard(true_use_card)
        if_squad = is_squad(true_use_card)
        if_sister = is_sister(true_use_card)
        if_bomb = is_bomb(true_use_card)
        if if_string == True:
            return Rope(true_use_card[0], len(true_use_card))
            # return [{"kind": "string"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_onecard == True:
            return Single(true_use_card[0])
            # return [{"kind": "onecard"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_twocard == True:
            return Double(true_use_card[0])
            # return [{"kind": "twocard"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_threecard == True:
            return Triple(true_use_card[0])
            # return [{"kind": "threecard"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_squad == True:
            char = 0
            for i in true_use_card:
                if i == true_use_card[0]:
                    char += 1
            if char == 2:
                return Combine(true_use_card[2], 0)
                # return [{"kind": "squad"}, {"length": len(true_use_card)}, {"level": true_use_card[2]}]
            if char == 3:
                return Combine(true_use_card[0], 0)
                # return [{"kind": "squad"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_sister == True:
            return Sister(true_use_card[0], len(true_use_card)/2)
            # return [{"kind": "sister"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        if if_bomb == True:
            return Bomb(true_use_card[0], 0)
            # return [{"kind": "bomb"}, {"length": len(true_use_card)}, {"level": true_use_card[0]}]
        num -= 1
        if num >= 0:
            true_use_card.append(1)
            true_use_card.remove(14)
            true_use_card.sort(reverse=True)
    return InvalidCardType()


# def check_cards_if_has(who, whatcard):
#     global user1_card, user2_card, user3_card
#     list1 = []
#     test_who = []
#     for a in who:
#         test_who.append(a)
#
#     for b in whatcard:
#         list1.append(b)
#     information = 0
#     for every_num in list1:
#         for compare_num in test_who:
#             if every_num == str(compare_num):
#                 # test_who.remove(compare_num)
#                 information += 1
#                 break
#     if information == len(list1):
#         return True
#     else:
#         return False


class TestOk(unittest.TestCase):

    def test_squad_is_ok(self):
        # 三带二 通过
        use_card = "JJ2J2"
        self.assertCountEqual([{"kind": "squad"}, {"length": 5},
                               {"level": 11}], identify_your_card(use_card))
        use_card = "KAKKA"
        self.assertCountEqual([{"kind": "squad"}, {"length": 5},
                               {"level": 13}], identify_your_card(use_card))
        use_card = "3A3AA"
        self.assertCountEqual([{"kind": "squad"}, {"length": 5},
                               {"level": 14}], identify_your_card(use_card))
        use_card = "AAA22"
        self.assertCountEqual([{"kind": "squad"}, {"length": 5},
                               {"level": 14}], identify_your_card(use_card))
        use_card = "TTJTJ"
        self.assertCountEqual([{"kind": "squad"}, {"length": 5},
                               {"level": 10}], identify_your_card(use_card))
        # 三带二失败
        use_card = "TTKK"
        self.assertEqual("invalid input", identify_your_card(use_card))

        # # 测试姐妹
        # use_card = "TTJJ"
        # self.assertEqual("invalid input", identify_your_card(use_card))

    # def onecard_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #     return
    #
    # def twocard_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #
    #     return
    #
    # def threecard_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #     return
    #
    # def string_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #     return
    #
    # def sister_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #     return
    #
    # def bomb_is_ok(self):
    #     # 单牌成功
    #
    #     # 单牌失败
    #     return


# def remove_cards(who,whatcard):
#     for a in what
# deal_cards()
# show_cards()
#
#
# print(user1_card)
# print(user2_card)
# print(user3_card)
# use_card = input("which car do you want to use")
# print(identify_your_card(use_card))
# print(check_cards_if_has(user1_card,use_card))
# print(user1_card)

