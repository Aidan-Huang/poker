from poker import Poker
from player import Player
from card_type import CardType
from common import Common
import sys, os

# 确定牌堆，完成洗牌
poker = Poker()
poker.shuffle_deck()
# print(poker.deck)

# 加入玩家，完成发牌
aidan = Player("Aidan")
eric = Player("Eric")
npc = Player(Player.NPC_NAME)

poker.add_player(aidan)
poker.add_player(eric)
poker.add_player(npc)

poker.distribute_all()
aidan.hand_cards.sort()
eric.hand_cards.sort()
# print(aidan.hand_cards)
# print(eric.hand_cards)

# 确认出牌玩家
current_player = Poker.get_first_player()
current_type = None
current_type_player = None
has_cards_to_play = "yes"

def info_to_chang_player():
    global current_player
    # input("Ready to change to next player.")
    # os.system('clear')
    # input("Please let the screen to the next player ")
    current_player = Poker.get_next_human()
    # print(f"after change, current player is:{current_player.name}")

# 玩家出牌后（合法牌型），轮流接牌
# 哪位玩家手牌为空则判定获胜
while poker.get_winner() is None:
    print(f"player: {current_player.name}'s turn")
    print(current_player.hand_cards)

    if current_type is not None and current_player != current_type_player:
        print(f"current cards: {current_type}")
        # has_cards_to_play = input("Do you want to play cards against current?(Yes, No):").lower()
        # if has_cards_to_play == "no":
        #     current_type = None
        #     info_to_chang_player()
        #     continue

    cards = [int(x) for x in input("Please input cards you want to play:").split()]
    card_type = Poker.analyze_card(cards)
    # 出牌是否合法
    # 如果出牌，牌型有效并且手牌包含所有组成牌型牌
    # 如果压牌，牌型有效并且大于当前牌型并且手牌包含所有组成牌型牌
    if current_type is None:
        while card_type.name == CardType.CARD_TYPE_INVALID_TYPE or not Common.is_contain_sub_list(
                current_player.hand_cards, cards):
            cards = [int(x) for x in input("The cards your played is illegal, please try again:").split()]
            card_type = Poker.analyze_card(cards)
    else:
        while not card_type > current_type or not Common.is_contain_sub_list(
                current_player.hand_cards, cards):
            print("The cards your played is illegal")
            has_cards_to_play = input("Do you want to play cards against current?(Yes, No):").lower()
            if has_cards_to_play == "no":
                current_type = None
                info_to_chang_player()
                break
            else:
                cards = [int(x) for x in input("Please input cards you want to play:").split()]
                card_type = Poker.analyze_card(cards)

    if has_cards_to_play == "no":
        has_cards_to_play = "yes"
        continue

    current_player.play_a_type(card_type)
    current_type = card_type
    current_type_player = current_player
    info_to_chang_player()


print(f"{poker.get_winner().name} win!")


