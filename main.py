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

# Define the piece values for scoring purposes
PIECE_VALUES = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
    "K": 0
}

# Define the colors of the pieces
WHITE = "white"
BLACK = "black"

# Define the current player (white goes first)
current_player = WHITE

# Define a function to display the chessboard in the console
def display_board(board):
    for row in board:
        print("+---+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+---+")

# Define a function to get the color of a piece
def get_piece_color(piece):
    if piece.isupper():
        return WHITE
    else:
        return BLACK
