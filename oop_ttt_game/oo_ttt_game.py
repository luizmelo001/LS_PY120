import random

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=" "):
        self._marker = marker

    @property
    def marker(self):
        return self._marker     
    
    @marker.setter
    def marker(self, value):
        if value in (Square.INITIAL_MARKER, Square.HUMAN_MARKER, Square.COMPUTER_MARKER):
            self._marker = value
        else:
            raise ValueError("Invalid marker. Use ' ', 'X', or 'O'.")

    def __str__(self):
        return self.marker

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}
    
    def display(self):
        print("\n")
        for i in range(3):
            print(f"  {self.squares[1 + i*3]}  |  {self.squares[2 + i*3]}  |  {self.squares[3 + i*3]}  ")
            if i < 2:
                print("-----+-----+-----")
        print("\n")

    def mark_square(self, square_number, marker):
        self.squares[square_number].marker = marker
      

class Player:
    def __init__(self, marker):
        self.marker = marker

class Human(Player):
    def __init__(self, marker=Square.HUMAN_MARKER):
        super().__init__(marker)

class Computer(Player):
    def __init__(self, marker=Square.COMPUTER_MARKER):
        super().__init__(marker)

class TTTGame:

    def __init__(self):
        self.board = Board() #example of composition
        self.human = Human(Square.HUMAN_MARKER)
        self.computer = Computer(Square.COMPUTER_MARKER)

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing! Goodbye!")

    def human_moves(self):
        choice = None

        while True:
            # Get a list of available square numbers (keys where marker is INITIAL_MARKER)
            available_squares = [key for key, square in self.board.squares.items() if square.marker == Square.INITIAL_MARKER]
            available_squares_str = ', '.join(map(str, available_squares))
            choice = int(input(f"Choose one of the available squares: {available_squares_str}: "))
    
            if choice in self.board.squares and self.board.squares[choice].marker == Square.INITIAL_MARKER:
                self.board.mark_square(choice, self.human.marker)
                break
            else:
                print("Invalid choice. Please try again.")

     
    def computer_moves(self):
        available_squares = [key for key, square in self.board.squares.items() if square.marker == Square.INITIAL_MARKER]
        choice = random.choice(available_squares)
        self.board.mark_square(choice, self.computer.marker)    

    def play(self):
        self.display_welcome_message()

        while True:
            self.board.display()

            self.human_moves()
            self.board.display()
            #if self.check_winner():
            #    self.display_winner()
            #    break

           # if self.is_board_full():
           #    self.display_draw()
           #     break
            # Computer's turn
            self.computer_moves()
            self.board.display()
            break
        self.board.display()
        self.display_results() 
        self.display_goodbye_message()

   
ttt = TTTGame()
ttt.play()
