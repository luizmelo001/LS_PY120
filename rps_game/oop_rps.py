
"""Rock Paper Scissors game implemented using object-oriented programming."""

import random

class Player:
    """Base class for players in the Rock Paper Scissors game."""
    CHOICES = ['rock', 'paper', 'scissors']
    def __init__(self):
        # A player has choices and a move
        self.move = None


class Human(Player):
    """A player that chooses moves via user input."""
    super().__init__()

    def choose(self):
        """Prompt the user to choose a move and set self.move."""
        while True:
            choice = input('Choose your move (rock, paper, scissors): ').lower()
            if choice in Player.CHOICES:
                break
            print("Invalid move. Please try again.")
        self.move = choice


class Computer(Player):
    """A player that chooses moves randomly."""
    super().__init__()

    def choose(self):
        """Randomly select a move and set self.move."""
        self.move = random.choice(Player.CHOICES)

class Rule:
    """Manages the rules for determining the winner in Rock Paper Scissors."""
    winning_rules = {
            ('rock', 'scissors'): 'rock crushes scissors',
            ('paper', 'rock'): 'paper covers rock',
            ('scissors', 'paper'): 'scissors cut paper'
        }


    def compare(self, human_move, computer_move):
        """Compare human and computer moves to determine the winner."""
        if human_move == computer_move:
            print("It's a tie!")
        elif (human_move, computer_move) in self.winning_rules:
            print(f"You win: {self.winning_rules[(human_move, computer_move)]}!")
        else:
            # Infer the computer's winning message by reversing the moves
            reverse_key = (computer_move, human_move)
            message = self.winning_rules.get(reverse_key, f"{computer_move} beats {human_move}")
            print(f"Computer wins: {message}!")


class RPSGame(Rule):
    """Main game class that orchestrates the Rock Paper Scissors game."""
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        """Display the welcome message for the game."""
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        """Display the goodbye message when the game ends."""
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        """Display the players' moves and the game result."""
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'Player chose: {human_move}')
        print(f'Computer chose: {computer_move}')

        self.compare(human_move, computer_move)

    def _play_again(self):
        """Ask if the user wants to play another round."""
        while True:
            play_again = input('Do you want to play again? (yes/no): ').lower()
            if play_again in ['yes', 'no']:
                return play_again == 'yes'
            print("Invalid input. Please enter 'yes' or 'no'.")

    def _play_round(self):
        """Play a single round of the game."""
        self._human.choose()
        self._computer.choose()
        self._display_winner()

    def play(self):
        """Run the main game loop."""
        self._display_welcome_message()
        while True:
            self._play_round()
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()
