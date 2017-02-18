#Python tic tac toe console game with basic AI
import copy
w, h = 3, 3; #Width and height of the game field
playingField = [[" " for x in range(w)] for y in range(h)]

playerChar = "x"
cpuChar = "O"
playerTurn = True
playerX = 0
playerY = 0
cpuX = 0
cpuY = 0
gameOver = False
def draw( ):
    print("|" + playingField[0][0] + "|" +  playingField[1][0] + "|" +  playingField[2][0] + "|")
    print("|" + playingField[0][1] + "|" +  playingField[1][1] + "|" +  playingField[2][1] + "|")
    print("|" + playingField[0][2] + "|" +  playingField[1][2] + "|" +  playingField[2][2] + "|")

def checkVictory(board, x, y):
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
    return False

def checkSpace(x, y):
    if(playingField[x][y] == " "):
        return True
    else:
        return False
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
                    print(checkVictory(copy,cpuX,cpuY))
                    cpuX = x
                    cpuY = y
                    playingField[cpuX][cpuY] = cpuChar

    #check if the player can win in the next turn

    #Try to take the center position
    if playingField[1][1] == " ":
        cpuX = 1
        cpuY = 1
        playingField[cpuX][cpuY] = cpuChar

while(not gameOver):
    if(playerTurn):
        print("Enter XCords(0-2):")
        playerX = input()
        print("Enter YCords(0-2):")
        playerY = input()
        playerX = int(playerX)
        playerY = int(playerY)
        playingField[playerX][playerY] = playerChar
        playerTurn = False
        draw()
        print(checkVictory(playingField,playerX,playerY))
    else:
        cpuPlayer()
        draw()
        playerTurn = True

    if(checkVictory(playingField,playerX,playerY) and playerTurn):
        print("You Won")
        gameOver = True
