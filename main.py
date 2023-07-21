import random

# Card Class - suit and rank of each card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

    # Deck Class - will hold all possible card suit and ranks
class Deck:
    def __init__(self):
        self.cards =[]
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "K", "value": 10},
                {"rank": "Q", "value": 10},
            ]
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
                
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
            
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

# Hand Class - will work out the player and dealer hands 
class Hand:
    def __init__(self, dealer=False):
            self.cards = []
            self.value = 0
            self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list)
        
    def calculate_value(self):
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        
        # Ace can 1 or 11, this makes the value of an Ace worth 1 if value is greater than 21
        if has_ace and self.value > 21:
            self.value -= 10
            
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackhack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                and not show_all_dealer_cards and not self.is_blackhack():
                    print("Hidden")
            else:
                print(card)
        
        if not self.dealer:
            print("Value:", self.get_value())
        print()