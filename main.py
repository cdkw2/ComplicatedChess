# Define the initial state of the chessboard
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Define a function to display the chessboard in the console
def display_board(board):
    for row in board:
        print("+---+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+---+")

# Define a function to move a piece on the chessboard
def move_piece(board, from_square, to_square):
    from_rank, from_file = from_square
    to_rank, to_file = to_square
    piece = board[from_rank][from_file]
    board[from_rank][from_file] = " "
    board[to_rank][to_file] = piece

while True:
    display_board(board)
    from_square = input("Enter the square of the piece you want to move (e.g. 'e2'): ")
    to_square = input("Enter the square you want to move the piece to (e.g. 'e4'): ")
    from_rank, from_file = ord(from_square[1]) - 49, ord(from_square[0]) - 97
    to_rank, to_file = ord(to_square[1]) - 49, ord(to_square[0]) - 97
    move_piece(board, (from_rank, from_file), (to_rank, to_file))
