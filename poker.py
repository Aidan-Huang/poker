class Poker():

    cards_num = 54

    def __str__(self) -> str:
        return f"Poker: {self.cards_num} cards"

    def is_sister(self, cards):
        if len(cards) < 4:
            return False
        elif len(cards) % 2 != 0:
            return False
        return True



poker = Poker()

print(poker)