
class Square:
    def __init__(self, marker=" "):
        self.marker = marker

    def __str__(self):
        return self.marker

class Board:
    def __init__(self):
        self.squares = {
            1: "O",
            2: Square(),
            3: "X",
            4: Square(),
            5: Square(),
            6: Square(),
            7: Square(),
            8: Square(), 
            9: Square(),
        }

    def display(self):
        print("\n")
        for i in range(3):
            print(f"  {self.squares[1 + i*3]}  |  {self.squares[2 + i*3]}  |  {self.squares[3 + i*3]}  ")
            if i < 2:
                print("-----+-----+-----")
        print("\n")

class TTTGame:

    def __init__(self):
        self.board = Board() #example of composition

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing! Goodbye!")

    def play(self):
        self.display_welcome_message()

        while True:
            self.board.display()

            self.get_player_move()
            if self.check_winner():
                self.display_winner()
                break

            if self.is_board_full():
                self.display_draw()
                break
            break
        self.board.display()
        self.display_results() 
        self.display_goodbye_message()

   


ttt = TTTGame()
ttt.board.display()
