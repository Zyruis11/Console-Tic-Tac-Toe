#Python tic tac toe console game with basic AI
import copy
import player
w, h = 3, 3; #Width and height of the game field
playingField = [[" " for x in range(w)] for y in range(h)]

cpuChar = "O"
cpuX = 0
cpuY = 0
gameOver = False
def draw( ):
    print("|" + playingField[0][0] + "|" +  playingField[1][0] + "|" +  playingField[2][0] + "|")
    print("|" + playingField[0][1] + "|" +  playingField[1][1] + "|" +  playingField[2][1] + "|")
    print("|" + playingField[0][2] + "|" +  playingField[1][2] + "|" +  playingField[2][2] + "|")

def checkVictory(board, x, y):
    if(board[x][y] != " "):
        #check if previous move caused a win on vertical line
        if board[0][y] == board[1][y] == board [2][y]:
            return True

        #check if previous move caused a win on horizontal line
        if board[x][0] == board[x][1] == board [x][2]:
            return True

        #check if previous move was on the main diagonal and caused a win
        if x == y and board[0][0] == board[1][1] == board [2][2]:
            return True

        #check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and board[0][2] == board[1][1] == board [2][0]:
            return True
    else:
        return False

def checkSpace(x, y):
    if(playingField[x][y] == " "):
        return True
    else:
        return False
def checkFullBoard(board):
        for y in range(0,3):
            for x in range(0,3):
                if board[x][y] == " ":
                    print("not full")
                    return False
                else:
                    return True
def makeMove(x,y,char):
    playingField[x][y] = char

def copyBoard(board):
    return copy.deepcopy(board)
#clone the board then check
def cpuPlayer():
    # #check if it can win in the next turn
    for y in range(0,3):
        for x in range(0,3):
            copy = copyBoard(playingField)
            if checkSpace(x,y):
                copy[x][y] = cpuChar
                if checkVictory(copy,x,y):
                    cpuX = x
                    cpuY = y
                    playingField[cpuX][cpuY] = cpuChar
                    return

    #check if the player can win in the next turn
    for y in range(0,3):
        for x in range(0,3):
            copy = copyBoard(playingField)
            if checkSpace(x,y):
                copy[x][y] = player.playerChar
                if checkVictory(copy,x,y):
                    cpuX = x
                    cpuY = y
                    playingField[cpuX][cpuY] = cpuChar
                    return
    #Try to take the center position or one of the corners
    if playingField[1][1] == " ":
        cpuX = 1
        cpuY = 1
        playingField[cpuX][cpuY] = cpuChar
        return
    elif playingField[0][0] == " ":
        cpuX = 0
        cpuY = 0
        playingField[cpuX][cpuY] = cpuChar
        return
    elif playingField[2][0] == " ":
        cpuX = 2
        cpuY = 0
        playingField[cpuX][cpuY] = cpuChar
        return
    elif playingField[0][2] == " ":
        cpuX = 0
        cpuY = 2
        playingField[cpuX][cpuY] = cpuChar
        return
    elif playingField[2][2] == " ":
        cpuX = 2
        cpuY = 2
        playingField[cpuX][cpuY] = cpuChar
        return

while(not gameOver):
    if(player.playerTurn):
        x,y = player.playerMove()
        makeMove(x,y,player.playerChar)
        print("Your Move")
        draw()
        player.playerTurn = False
    else:
        cpuPlayer()
        print("Computer's Move")
        draw()
        player.playerTurn = True
        print(cpuX, cpuY)

    if checkVictory(playingField,player.playerX,player.playerY):
        print("You Won")
        gameOver = True
    elif checkVictory(playingField,cpuX,cpuY):
        print("You Lost")
        print("Computers last turn",cpuX, cpuY)
        gameOver = True
    elif checkFullBoard(playingField):
        print("It's a tie")
        gameOver = True
