def drawBoard(board):
    blank_board = '|     '*3+'|'
    edge_board = '+-----'*3+'+'
    def drawLine(board_line):
        insert_sym = "|"
        print(blank_board)
        print("| ",board_line[0]," | ",board_line[1]," | ",board_line[2]," |")
        print(blank_board)
        print(edge_board)
    print(edge_board)
    drawLine(board[7:10])
    drawLine(board[4:7])
    drawLine(board[1:4])

def playerGenerator(name):
    playerSym = ""
    while not( playerSym == "X" or playerSym == "O"):
        if playerSym =="":
            print(name," , Do you want to use X or O")
        else:
            print("Please type X or O")
        playerSym = input().upper()
    if playerSym == "X":
        return ["X","O"]
    elif playerSym =="O":
        return ["O","X"]

def isSpaceFree(board,move):
    return board[move] == '' or board[move] in "1 2 3 4 5 6 7 8 9".split()

def isWinner(board, playerSym):
    return ((board[7] == playerSym and board[8] == playerSym and board[9] == playerSym) or 
    (board[4] == playerSym and board[5] == playerSym and board[6] == playerSym) or 
    (board[1] == playerSym and board[2] == playerSym and board[3] == playerSym) or 
    (board[7] == playerSym and board[4] == playerSym and board[1] == playerSym) or 
    (board[8] == playerSym and board[5] == playerSym and board[2] == playerSym) or
    (board[9] == playerSym and board[6] == playerSym and board[3] == playerSym) or
    (board[7] == playerSym and board[5] == playerSym and board[3] == playerSym) or
    (board[9] == playerSym and board[5] == playerSym and board[1] == playerSym))

def playerMove(board,playerSym):
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split():
        print("What's your next move")
        move = input()
        try:
            if not isSpaceFree(board, int(move)):
                print("Space %s is alreay taken"%move)
                move =''
                continue
        except:
            print("Type a vaild number (1-9)")
            continue
    board[int(move)] = playerSym
    return isWinner(board,playerSym)
    
def playAgain():
    print("Do you want to play again?")
    return input().lower().startswith('y')

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

if __name__ == "__main__":
    print("Let's Tic Tac Toe!")
    while True:
        print("Type your name please")
        playerOneName = input()
        print("Thanks,",playerOneName)
        print("Type your name please")
        playerTwoName = input()
        print("Thanks,",playerTwoName)
        theBoard = "0 1 2 3 4 5 6 7 8 9".split()
        playerOne, playerTwo = playerGenerator(playerOneName)
        playerSym=(playerOne,playerTwo)
        playerName=(playerOneName,playerTwoName)
        print(playerOneName," play first")
        turn = 0
        gameIsPlaying = True

        while gameIsPlaying:
            drawBoard(theBoard)
            current_player = playerSym[turn]
            current_playerName = playerName[turn]
            print(current_playerName,"\'s turn")

            if playerMove(theBoard,current_player):
                drawBoard(theBoard)
                print(current_playerName," wins!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("A draw seems the best!")
                else:
                    turn = (turn+1)%2
        if not playAgain():
            break






