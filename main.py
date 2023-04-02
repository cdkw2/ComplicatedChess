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

# Define a function to get the valid diagonal moves for a queen
def get_queen_diagonal_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "Q":
        # Queen diagonal moves
        # Bottom right diagonal moves
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
        # Top right diagonal moves
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
        # Bottom left diagonal moves
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
        # Top left diagonal moves
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

# Define a function to get the valid horizontal and vertical moves for a queen
def get_queen_hv_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "Q":
        # Queen horizontal and vertical moves
        # Horizontal moves
        i = from_square[0]
        j = from_square[1] + 1
        while j < 8:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            j += 1
        j = from_square[1] - 1
        while j >= 0:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            j -= 1
        # Vertical moves
        i = from_square[0] + 1
        j = from_square[1]
        while i < 8:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i += 1
        i = from_square[0] - 1
        while i >= 0:
            if board[i][j] == " ":
                valid_moves.append((i, j))
            elif get_piece_color(board[i][j]) != color:
                valid_moves.append((i, j))
                break
            else:
                break
            i -= 1
    return valid_moves

# Define a function to get the valid moves for a king
def get_king_moves(board, from_square):
    valid_moves = []
    piece = board[from_square[0]][from_square[1]]
    color = get_piece_color(piece)
    if piece == "K":
        # King moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                row = from_square[0] + i
                col = from_square[1] + j
                if row >= 0 and row < 8 and col >= 0 and col < 8:
                    if board[row][col] == " " or get_piece_color(board[row][col]) != color:
                        valid_moves.append((row, col))
    return valid_moves

# Define a function to evaluate the current board state for the AI player
def evaluate_board(board):
    # This is a very basic evaluation function that simply counts the number of pieces on the board for the AI player
    score = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == "P":
                score -= 1
            elif piece == "N" or piece == "B":
                score -= 3
            elif piece == "R":
                score -= 5
            elif piece == "Q":
                score -= 9
            elif piece == "K":
                score -= 100
            elif piece == "p":
                score += 1
            elif piece == "n" or piece == "b":
                score += 3
            elif piece == "r":
                score += 5
            elif piece == "q":
                score += 9
            elif piece == "k":
                score += 100
    return score

# Define a function to get the best move for the AI player using the Minimax algorithm
def get_ai_move(board, depth):
    def minimax(board, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return evaluate_board(board), None
        if maximizing_player:
            max_score = float("-inf")
            best_move = None
            for move in get_all_valid_moves(board, "w"):
                result_board = make_move(board, move)
                score, _ = minimax(result_board, depth - 1, alpha, beta, False)
                if score > max_score:
                    max_score = score
                    best_move = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score, best_move
        else:
            min_score = float("inf")
            best_move = None
            for move in get_all_valid_moves(board, "b"):
                result_board = make_move(board, move)
                score, _ = minimax(result_board, depth - 1, alpha, beta, True)
                if score < min_score:
                    min_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score, best_move
    _, best_move = minimax(board, depth, float("-inf"), float("inf"), True)
    return best_move
