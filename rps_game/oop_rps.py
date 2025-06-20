import random

class Player:
    CHOICES = ['rock', 'paper', 'scissors']
    def __init__(self, player_type):
        # Type of player: 'human' or 'computer'
        # A player has choices and a move
        self._player = player_type.lower()
        self.move = None

    def choose(self):
        if self._player == 'human':
            while True:
                choice = input('Choose your move (rock, paper, scissors): ').lower()
                if choice in Player.CHOICES:
                    break
                else:
                    print("Invalid move. Please try again.")
            self.move = choice
        else:
            self.move = random.choice(Player.CHOICES)

    def _display_welcome_message(self):
        print(f'Welcome to Rock Paper Scissors')

    def _display_goodbye_message(self):
        print(f'Thanks for playing Rock Paper Scissors. Goodbye!')

class Move:
    def __init__(self):
        # This seems like we need something to keep track
        # of the choice... a move object can be "paper", "rock" or "scissors"
        pass

class Rule:
    def __init__(self):
        # not sure what the "state" of a rule object should be
        pass

    # not sure where "compare" goes yet
    def compare(self, human_move, computer_move):
        if human_move == computer_move:
            print("It's a tie!")
        elif (human_move == 'rock' and computer_move == 'scissors') or \
             (human_move == 'paper' and computer_move == 'rock') or \
             (human_move == 'scissors' and computer_move == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")


class RPSGame(Rule):
    def __init__(self):
        self._human = Player("human")
        self._computer = Player("computer")

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'Player chose: {human_move}')
        print(f'Computer chose: {computer_move}')

        self.compare(human_move, computer_move)

    def _play_again(self):
        while True:
            play_again = input('Do you want to play again? (yes/no): ').lower()
            if play_again in ['yes', 'no']:
                return play_again == 'yes'
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def _play_round(self):
        self._human.choose()
        self._computer.choose()
        self._display_winner()

    def play(self):
        self._display_welcome_message()
        while True:
            self._play_round()
            if not self._play_again():
                break
        self._display_goodbye_message()

RPSGame().play()
