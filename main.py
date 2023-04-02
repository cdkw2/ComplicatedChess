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

# Play the game!
while True:
    display_board(board)
    from_square = input("Enter the square of the piece you want to move (e.g. 'e2'): ")
    to_square = input("Enter the square you want to move the piece to (e.g. 'e4'): ")
    from_rank, from_file = ord(from_square[1]) - 49, ord(from_square[0]) - 97
    to_rank, to_file = ord(to_square[1]) - 49, ord(to_square[0]) - 97
    move_piece(board, (from_rank, from_file), (to_rank, to_file))

# Define a function to get the valid moves for a pawn
def get_valid_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "P":
        # Pawn moves
        if color == WHITE:
            if from_square[0] == 6:
                if board[4][from_square[1]] == " " and board[5][from_square[1]] == " ":
                    valid_moves.append((4, from_square[1]))
            if from_square[0] > 0 and board[from_square[0] - 1][from_square[1]] == " ":
                valid_moves.append((from_square[0] - 1, from_square[1]))
            if from_square[0] > 0 and from_square[1] > 0 and get_piece_color(board[from_square[0] - 1][from_square[1] - 1]) == BLACK:
                valid_moves.append((from_square[0] - 1, from_square[1] - 1))
            if from_square[0] > 0 and from_square[1] < 7 and get_piece_color(board[from_square[0] - 1][from_square[1] + 1]) == BLACK:
                valid_moves.append((from_square[0] - 1, from_square[1] + 1))
        else:
            if from_square[0] == 1:
                if board[3][from_square[1]] == " " and board[2][from_square[1]] == " ":
                    valid_moves.append((2, from_square[1]))
            if from_square[0] < 7 and board[from_square[0] + 1][from_square[1]] == " ":
                valid_moves.append((from_square[0] + 1, from_square[1]))
            if from_square[0] < 7 and from_square[1] > 0 and get_piece_color(board[from_square[0] + 1][from_square[1] - 1]) == WHITE:
                valid_moves.append((from_square[0] + 1, from_square[1] - 1))
            if from_square[0] < 7 and from_square[1] < 7 and get_piece_color(board[from_square[0] + 1][from_square[1] + 1]) == WHITE:
                valid_moves.append((from_square[0] + 1, from_square[1] + 1))
    return valid_moves

# Define a function to get the valid moves for a rook piece
def get_rook_valid_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "R":
        # Rook moves
        # Horizontal moves
        for i in range(from_square[1] + 1, 8):
            if board[from_square[0]][i] == " ":
                valid_moves.append((from_square[0], i))
            elif get_piece_color(board[from_square[0]][i]) != color:
                valid_moves.append((from_square[0], i))
                break
            else:
                break
        for i in range(from_square[1] - 1, -1, -1):
            if board[from_square[0]][i] == " ":
                valid_moves.append((from_square[0], i))
            elif get_piece_color(board[from_square[0]][i]) != color:
                valid_moves.append((from_square[0], i))
                break
            else:
                break
        # Vertical moves
        for i in range(from_square[0] + 1, 8):
            if board[i][from_square[1]] == " ":
                valid_moves.append((i, from_square[1]))
            elif get_piece_color(board[i][from_square[1]]) != color:
                valid_moves.append((i, from_square[1]))
                break
            else:
                break
        for i in range(from_square[0] - 1, -1, -1):
            if board[i][from_square[1]] == " ":
                valid_moves.append((i, from_square[1]))
            elif get_piece_color(board[i][from_square[1]]) != color:
                valid_moves.append((i, from_square[1]))
                break
            else:
                break
    return valid_moves

# Define a function to get the valid moves for a horse piece
def get_horse_valid_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "N":
        # Horse moves
        moves = [(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
        for move in moves:
            to_square = (from_square[0]+move[0], from_square[1]+move[1])
            if 0 <= to_square[0] < 8 and 0 <= to_square[1] < 8:
                if board[to_square[0]][to_square[1]] == " " or get_piece_color(board[to_square[0]][to_square[1]]) != color:
                    valid_moves.append(to_square)
    return valid_moves

# Define a function to get the valid moves for a bishop piece
def get_bishop_valid_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "B":
        # Bishop moves
        # Diagonal moves - bottom right
        i = from_square[0] + 1
        j = from_square[1] + 1
        while i < 8 and j < 8:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i += 1
            j += 1
        # Diagonal moves - top right
        i = from_square[0] - 1
        j = from_square[1] + 1
        while i >= 0 and j < 8:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j += 1
        # Diagonal moves - bottom left
        i = from_square[0] + 1
        j = from_square[1] - 1
        while i < 8 and j >= 0:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i += 1
            j -= 1
        # Diagonal moves - top left
        i = from_square[0] - 1
        j = from_square[1] - 1
        while i >= 0 and j >= 0:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j -= 1
    return valid_moves
