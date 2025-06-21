
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
    def __init__(self):
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
    def __init__(self):
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

    def __init__(self):
        self.max_score = 5
        self.human_score = 0
        self.computer_score = 0


    def compare(self, human_move, computer_move):
        """Compare human and computer moves to determine the winner. Returns the winner and updates score"""
        if human_move == computer_move:
            print("It's a tie!")
            return "tie"
        elif (human_move, computer_move) in self.winning_rules:
            self.human_score += 1
            print(f"You win: {self.winning_rules[(human_move, computer_move)]}!")
            return "human"
        else:
            # Infer the computer's winning message by reversing the moves
            self.computer_score += 1
            reverse_key = (computer_move, human_move)
            message = self.winning_rules.get(reverse_key, f"{computer_move} beats {human_move}")
            print(f"Computer wins: {message}!")
            return "computer"
        
    def display_scores(self):
        """Display the current scores."""
        print(f"Score - Player: {self.human_score}, Computer: {self.computer_score}")

    def get_winner(self):
        """Returne the overall game winner."""
        if self.human_score >= self.max_score:
            return "Player"
        
        if self.computer_score >= self.max_score:
            return "Computer"
        
    def is_game_over(self):
        """Check if either player has reached the max score"""
        return self.human_score == self.max_score or self.computer_score == self.max_score


class RPSGame(Rule):
    """Main game class that orchestrates the Rock Paper Scissors game."""
    def __init__(self):
        super().__init__() # Initialize Rule's scorekeeping
        self._human = Human()
        self._computer = Computer()
        self.move_history = [] # List to store move history
        self.round_count = 0 # Track current round

    def _display_welcome_message(self):
        """Display the welcome message for the game."""
        print('Welcome to Rock Paper Scissors!')
        print(f'First to {self.max_score} points wins!')

    def _display_goodbye_message(self):
        """Displays the winner and the goodbye message when the game ends."""
        print(f'Final Score - Player: {self.human_score}, Computer: {self.computer_score}')

        winner = self.get_winner()
        if winner:
            print(f"{winner} wins the game!")
        else:
            print('Game ended without a winner.')

        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_move_history(self):
        """Display the history of moves made during the round."""
        if not self.move_history:
            print("No moves have been made yet.")
            return
        print("\nMove History:")
        print("Round | Human   | Computer")
        print("------|---------|---------")
        for round_num, human_move, computer_move in self.move_history:
            print(f"{round_num:<6}| {human_move:<7} | {computer_move:<8}")

    def _display_winner(self):
        """Display the players' moves and the game result."""
        human_move = self._human.move
        computer_move = self._computer.move
        print(f'Player chose: {human_move}')
        print(f'Computer chose: {computer_move}')
        self.compare(human_move, computer_move)
        self.display_scores()

    def _play_again(self):
        """Ask if the user wants to play another round."""
        while True:
            play_again = input('Do you want to play again? (yes/no): ').lower()
            if play_again in ['yes', 'no']:
                return play_again == 'yes'
            print("Invalid input. Please enter 'yes' or 'no'.")

    def _play_round(self):
        """Play a single round of the game."""
        self.round_count += 1
        self._human.choose()
        self._computer.choose()
        self._display_winner()
        #add moves to history
        self.move_history.append((self.round_count, self._human.move, self._computer.move))
        self._display_move_history()

    def play(self):
        """Run the main game loop."""
        self._display_welcome_message()
        while True:
            self._play_round()
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()
