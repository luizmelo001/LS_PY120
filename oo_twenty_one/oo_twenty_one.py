"""Twenty-One (Blackjack) game implementation using object-oriented programming."""

import random

class Card:
    """Represents a single playing card."""
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, rank, suit):
        #rank and suit
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Return a string representation of the card."""
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
       self.cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    def deal(self):
        """Deal and return a random card from the deck."""
        if not self.cards:
            self.cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
        return self.cards.pop(random.randrange(len(self.cards)))

class Participant:
    """Base class for game participants (Player and Dealer)."""
    def __init__(self):
        """Initialize a participant with an empty hand."""
        self.hand = []
        self.stayed = False

    def hit(self, deck):
        """Add a card to the participant's hand."""
        card = deck.deal()
        self.hand.append(card)

    def stay(self):
        """Mark the participant as staying."""
        self.stayed = True

    def is_busted(self):
        """Check if the participant's score exceeds 21."""
        return self.score() > 21
    
    def score(self):
        """Calculate the participant's score, adjusting for Aces."""
        score = sum(Card.VALUES[card.rank] for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')
        while score > 21 and num_aces > 0:
            score -= 10
            num_aces -= 1
        return score

class Player(Participant):
    """Represents the human player."""
    def __init__(self):
        super().__init__()
        self.money = 5
                

class Dealer(Participant):
    """Represents the dealer."""
    def __init__(self):
        """Initialize the dealer."""
        super().__init__()
        self.hidden = True

    def hide(self):
        """Mark the dealer's first card as hidden."""
        self.hidden = True

    def reveal(self):
        """Reveal the dealer's hidden card."""
        self.hidden = False

    def deal(self, deck, player):
        """Deal two cards to the player and dealer."""
        for _ in range(2):
            player.hit(deck)
            self.hit(deck)

class TwentyOneGame:
    """Manages the Twenty-One game logic and flow."""
    def __init__(self):
        """Initialize the game with a deck, player, and dealer."""
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        """Run the main game loop."""
        self.display_welcome_message()

        while self.player.money > 0 and self.player.money < 10:
            self.deck = Deck() # Reset the deck for each game
            self.player.hand = []  # Reset player's hand
            self.dealer.hand = []  # Reset dealer's hand
            self.player.stayed = False  
            self.dealer.stayed = False
            self.dealer.hide()
            self.deal_cards()
            self.show_cards()
            self.player_turn()
            if not self.player.is_busted():
                self.dealer_turn()
            self.display_result()
            if not self.play_again():
                break   

        self.display_goodbye_message()

    def deal_cards(self):
        """Run the main game loop."""
        self.dealer.deal(self.deck, self.player)

    def show_cards(self):
        """Display the dealer's and player's hands."""
        print("\nDealer's Hand:")
        if self.dealer.hidden:
            print(f"{self.dealer.hand[0]} and [Hidden Card]")
        else:
            print(", ".join(str(card) for card in self.dealer.hand))
            print(f"Dealer's Score: {self.dealer.score()}")

        print("\nPlayer's Hand:")
        print(", ".join(str(card) for card in self.player.hand))
        print(f"Player's Score: {self.player.score()}")
        print(f"Player's Money: ${self.player.money}")

    def player_turn(self):
        """Handle the player's turn."""
        while not self.player.stayed and not self.player.is_busted():
            choice = input("Do you want to hit (h) or stay (s)? ").strip().lower()
            if choice in ('h', 'hit'):
                self.player.hit(self.deck)
                self.show_cards()
            elif choice in ('s', 'stay'):
                self.player.stay()
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def dealer_turn(self):
        """Handle the dealer's turn."""
        self.dealer.reveal()
        self.show_cards()

        while self.dealer.score() < 17:
            print("Dealer hits.")
            self.dealer.hit(self.deck)
            self.show_cards()

    def display_welcome_message(self):
        """Display the welcome message."""
        print("Welcome to Twenty-One!")

    def display_goodbye_message(self):
        """Display the goodbye message."""
        print("Thanks for playing Twenty-One! Goodbye!")

    def display_result(self):
        """Display the game result and update player's money."""
        self.dealer.reveal()
        self.show_cards()   

        if self.player.is_busted():
            print("You busted! Dealer wins.")
        elif self.dealer.is_busted() or self.player.score() > self.dealer.score():
            print("You win!")
            self.player.money += 1
        elif self.player.score() < self.dealer.score():
            print("Dealer wins!")
            self.player.money -= 1
        else:
            print("It's a tie!")

    def play_again(self):
        """Ask the player if they want to play again."""

        if self.player.money == 0:
            print("You have no money left. Game over!")
            return
        
        if self.player.money >= 10:
            print("Congratulations! You have reached $10. You win the game!")
            return

        while True:
            choice = input("Do you want to play again? (y/n): ").strip().lower()
            if choice in ('y', 'yes'):
                return True
            elif choice in ('n', 'no'):
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

game = TwentyOneGame()
game.start()