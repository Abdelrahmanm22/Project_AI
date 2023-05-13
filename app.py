import numpy as np
COLUMNS = 7
ROWS = 6

def Build_board():
    board = np.zeros((6,7))
    return board


def SetPiece(board,row,col,piece):
    board[row][col] = piece

def isValid(board,col):
    if board[5][col] == 0:
        return True
    else:
        return False



def GetNextRow(board,col):
    for r in range(ROWS):
        if board[r][col]==0:
            return r



####to print board right(flip it)#############
def printBoard(board):
    print(np.flip(board,0))
####to print board right#############

#call function (Build_board)
board = Build_board()
printBoard(board)


def winning_move(board,piece):
    for c in range(COLUMNS-3):
        for r in range (ROWS):
            if board[r][c] == piece and board [r][c+1] == piece and board [r][c+2] == piece and board[r][c+3]:
                return True
#check vertical
    for c in range(COLUMNS):
        for r in range (ROWS-3):
            if board[r][c] == piece and board [r+1][c] == piece and board [r+2][c] == piece and board[r+3][c]:
                return True

#check + diagonal
    for c in range(COLUMNS-3):
        for r in range (ROWS-3):
            if board[r][c] == piece and board [r+1][c+1] == piece and board [r+2][c+2] == piece and board[r+3][c+3]:
                return True

#check - diagonal
    for c in range(COLUMNS-3):
        for r in range (ROWS-3):
          if board[r][c] == piece and board [r-1][c+1] == piece and board [r-2][c+2] == piece and board[r-3][c+3]:
                return True

switch=0 #to turn play to another player
GameOver = False
while  (GameOver==False):


    #Player 1 play:
    if switch == 0:
        select = int(input("Select (player 1) from 0-6: "))
        switch = 1
        if isValid(board,select):
            row =GetNextRow(board,select)
            SetPiece(board,row,select,1)
            if winning_move(board,1):
                print("Player 1 wins ")
                GameOver=True

        # print(select)

    # Player 2 play:
    else:
        select = int(input("Select (player 2) from 0-6: "))
        switch = 0
        if isValid(board,select):
            row = GetNextRow(board,select)
            SetPiece(board,row,select,2)
            if winning_move(board, 2):
                print("Player 2 wins ")
                GameOver = True


    printBoard(board)








