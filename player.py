#Class that controls the player
playerChar = "x"
playerTurn = True
playerX = 0
playerY = 0

def playerMove():
    print("Enter XCords(0-2):")
    playerX = input()
    print("Enter YCords(0-2):")
    playerY = input()
    playerX = int(playerX)
    playerY = int(playerY)
    print(playerX, playerY)
    return playerX,playerY
