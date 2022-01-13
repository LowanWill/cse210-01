

def main():
    player = player_turns("")
    board = game_board()
    while not (winner(board) or tie(board)):
        game_grid(board)
        input_move(player, board)
        player = player_turns(player)
    game_grid(board)
    print("Nicely done! Hope you enjoyed your game!")

def game_board():
    board = []
    for grid in range(16):
        board.append(grid + 1)
    return board

def game_grid(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}|{board[7]}")
    print("-+-+-+-")
    print(f"{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print("-+-+-+-+-")
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}")
    print()
    
def tie(board):
    for grid in range(16):
        if board[grid] != "x" and board[grid] != "o":
            return False
    return True 
    
def winner(board):
    return (board[0] == board[1] == board[2] == board[3] or
            board[4] == board[5] == board[6] == board[7] or
            board[8] == board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] == board[15] or
            board[0] == board[4] == board[8] == board[12] or
            board[1] == board[5] == board[9] == board[13] or
            board[2] == board[6] == board[10] == board[14] or
            board[3] == board[7] == board[11] == board[15] or
            board[0] == board[5] == board[10] == board[15] or
            board[3] == board[6] == board[9] == board[12])

def input_move(player, board):
    grid = int(input(f"It is {player}'s turn to choose a square (1-16): "))
    board[grid - 1] = player

def player_turns(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()