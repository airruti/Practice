board = [["-"]* 3 for i in range(3)]

p1 = "X"
p2 = "O"

def validate(x, y, board):
    if x > 2 or y > 2:
        print("Select a valid row/column")
        return False
    if x < 0 or y < 0: 
        print("Select a valid row/column")
        return False
    if (board[x][y]) != "-":
        print("taken")
        return False
    else: return True

def makeMove(x, y, player, board):
    if validate(x, y, board):
        board[x][y] = player
        return True
    else:
        print("Not a valid move")
        return False

    
def win(player, board):
    if board[0][0] == board[0][1] == board[0][2] == player:
        return True

    if board[1][0] == board[1][1] == board[1][2] == player:
        return True

    if board[2][0] == board[2][1] == board[2][2] == player:
        return True

    if board[0][0] == board[1][0] == board[2][0] == player:
        return True

    if board[0][1] == board[1][1] == board[2][1] == player:
        return True
    
    if board[0][2] == board[1][2] == board[2][2] == player:
        return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    
    if board[0][2] == board[1][1] == board[0][0] == player:
        return True
        
    else: return False

i = 0
while i < 9:
    for j in board:
        print (j)
    x_input = input(f"Select Row\n")
    y_input = input(f"Select Column\n")
    if makeMove(int(x_input), int(y_input), p1 if i % 2 == 0 else p2, board):
        i += 1
    elif not makeMove(int(x_input), int(y_input), p1 if i % 2 == 0 else p2, board):
        continue
    if win(p1 or p2, board):
        print(board)
        print(f"{p2 if i % 2 == 0 else p1} wins!")
        break

if i == 9: print("It's a tie!")