"""Tic Tac Toe game implementation using object-oriented programming."""

import random

class Square:
    """Represents a single square on the Tic Tac Toe board."""
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=" "):
        """Initialize a square with a marker (' ', 'X', or 'O')."""
        self._marker = marker

    @property
    def marker(self):
        """Get the square's marker."""
        return self._marker

    @marker.setter
    def marker(self, value):
        """Set the square's marker, ensuring it's valid."""
        if value in (Square.INITIAL_MARKER, Square.HUMAN_MARKER, Square.COMPUTER_MARKER):
            self._marker = value
        else:
            raise ValueError("Invalid marker. Use ' ', 'X', or 'O'.")

    def __str__(self):
        """Return the string representation of the square's marker."""
        return self.marker


class Board:
    """Represents the 3x3 Tic Tac Toe board."""

    def __init__(self):
        """Initialize the board with 9 empty squares."""
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        """Display the current state of the board."""
        print("\n")
        for i in range(3):
            print(f"  {self.squares[1 + i*3]}  |  {self.squares[2 + i*3]}  |  {self.squares[3 + i*3]}  ")
            if i < 2:
                print("-----+-----+-----")
        print("\n")

    def mark_square(self, square_number, marker):
        """Mark a square with the given marker."""
        self.squares[square_number].marker = marker


class Player:
    """Base class for Tic Tac Toe players."""

    def __init__(self, marker):
        """Initialize a player with a marker."""
        self.marker = marker


class Human(Player):
    """Represents the human player with marker 'X'."""

    def __init__(self, marker=Square.HUMAN_MARKER):
        """Initialize the human player."""
        super().__init__(marker)


class Computer(Player):
    """Represents the computer player with marker 'O'."""

    def __init__(self, marker=Square.COMPUTER_MARKER):
        """Initialize the computer player."""
        super().__init__(marker)


class TTTGame:
    """Manages the Tic Tac Toe game logic and flow."""
    WINNING_COMBINATIONS = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]

    def __init__(self):
        """Initialize the game with a board and players."""
        self.board = Board()
        self.human = Human(Square.HUMAN_MARKER)
        self.computer = Computer(Square.COMPUTER_MARKER)

    def display_welcome_message(self):
        """Display the welcome message for the game."""
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        """Display the goodbye message when the game ends."""
        print("Thanks for playing! Goodbye!")

    def human_moves(self):
        """Prompt the human player to choose a square and mark it."""
        while True:
            available_squares = [
                key for key, square in self.board.squares.items()
                if square.marker == Square.INITIAL_MARKER
            ]
            available_squares_str = ', '.join(map(str, available_squares))
            choice_input = input(
                f"Choose one of the available squares ({available_squares_str}): "
            )
            if choice_input.isdigit():
                choice = int(choice_input)
                if (choice in self.board.squares and
                        self.board.squares[choice].marker == Square.INITIAL_MARKER):
                    self.board.mark_square(choice, self.human.marker)
                    break
                print("Invalid choice. Square is taken or doesn't exist.")
            print("Invalid input. Please enter a number.")

    def computer_moves(self):
        """Select a random square for the computer and mark it."""
        available_squares = [
            key for key, square in self.board.squares.items()
            if square.marker == Square.INITIAL_MARKER
        ]
        choice = random.choice(available_squares)
        self.board.mark_square(choice, self.computer.marker)

    def is_game_over(self):
        """Check if the game is over (win or draw)."""
        return self.check_winner() or self.is_board_full()

    def is_board_full(self):
        """Check if the board is full (no empty squares)."""
        return all(square.marker != Square.INITIAL_MARKER
                   for square in self.board.squares.values())

    def check_winner(self):
        """Check if any player has three markers in a row, column, or diagonal."""
        for combination in TTTGame.WINNING_COMBINATIONS:
            if (self.board.squares[combination[0]].marker ==
                    self.board.squares[combination[1]].marker ==
                    self.board.squares[combination[2]].marker != Square.INITIAL_MARKER):
                return True
        return False

    def is_winner(self, player):
        """Check if the given player has won."""
        return any(
            self.board.squares[combo[0]].marker ==
            self.board.squares[combo[1]].marker ==
            self.board.squares[combo[2]].marker == player.marker
            for combo in TTTGame.WINNING_COMBINATIONS
        )

    def display_winner(self):
        """Display the game result (win or draw)."""
        if self.check_winner():
            if self.is_winner(self.human):
                print("Player wins!")
            elif self.is_winner(self.computer):
                print("Computer wins!")
        else:
            print("It's a draw!")

    def play(self):
        """Run the main game loop."""
        self.display_welcome_message()
        while True:
            self.board.display()
            self.human_moves()
            if self.is_game_over():
                self.board.display()
                self.display_winner()
                break
            self.computer_moves()
            if self.is_game_over():
                self.board.display()
                self.display_winner()
                break
        self.display_goodbye_message()


if __name__ == "__main__":
    ttt = TTTGame()
    ttt.play()

ttt = TTTGame()
ttt.play()
