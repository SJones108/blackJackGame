import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(1, 14):
                card = Card(suit, value)
                self.cards.append(card)
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)
        if card.value == 1 and self.value + 11 <= 21:
            self.value += 11
        elif card.value >= 10:
            self.value += 10
        else:
            self.value += card.value
            
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
    def play(self):
        while True:
            self.initial_deal()
            print(f"Player's Hand: {self.player_hand} ({self.player_hand.value})")
            print(f"Dealer's Hand: {self.dealer_hand.cards[0]}")
            while True:
                if self.player_hand.value > 21:
                    print("Bust! You lose.")
                    break
                action = input("Do you want to hit or stand? ")
                if action.lower() == "hit":
                    card = self.deck.deal_card()
                    print(f"Dealt: {card}")
                    self.player_hand.add_card(card)
                    print(f"Player's Hand: {self.player_hand} ({self.player_hand.value})")
                elif action.lower() == "stand":
                    break
                else:
                    print("Invalid action, please try again.")
            while self.dealer_hand.value < 17:
                card = self.deck.deal_card()
                print(f"Dealer dealt: {card}")
                self.dealer_hand.add_card(card)
                print(f"Player's Hand: {self.player_hand} ({self.player_hand.value})")
                print(f"Dealer's Hand: {self.dealer_hand} ({self.dealer_hand.value})")
            if self.dealer_hand.value > 21:
                print("Dealer bust! You win.")
            elif self.player_hand.value > self.dealer_hand.value:
                print("You win!")
            elif self.player_hand.value < self.dealer_hand.value:
                print("You lose.")
            else:
                print("It's a tie.")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() != "y":
                return
            self.deck = Deck()
            self.player_hand = Hand()
            self.dealer_hand = Hand()

    def initial_deal(self): #Starting of the game
        print("Welcome to Shirley's Blackjack Game!")
        for _ in range(2):
            card = self.deck.deal_card()
            self.player_hand.add_card(card)
            card = self.deck.deal_card()
            self.dealer_hand.add_card(card)

#This will run the game
game = Blackjack()
game.play()
