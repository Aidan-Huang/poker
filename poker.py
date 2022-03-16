class Poker():

    cards_num = 54

    def __str__(self) -> str:
        return f"Poker: {self.cards_num} cards"



poker = Poker()

print(poker)