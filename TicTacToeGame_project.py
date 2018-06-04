import random

# define a function display board
def displayBoard():
    # use print method how output display should be
    print("+---+---+---+")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("+---+---+---+")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("+---+---+---+")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("+---+---+---+")


# define tossSymbol function to find who wins in toss
def tossSymbol():
    # generate a random number it can be either 0 or 1
    ts = random.randint(0, 1)
    # return the result
    return ts

# define a winning condition
def isWinner(char):
    # Horizontal winning condition
    if board[0] == char and board[1] == char and board[2] == char:
        return True
    elif board[3] == char and board[4] == char and board[5] == char:
        return True
    elif board[6] == char and board[7] == char and board[8] == char:
        return True

    # Vertical winning condition
    elif board[0] == char and board[3] == char and board[6] == char:
        return True
    elif board[1] == char and board[4] == char and board[7] == char:
        return True
    elif board[2] == char and board[5] == char and board[8] == char:
        return True

    # Diagonal winning condition
    elif board[0] == char and board[4] == char and board[8] == char:
        return True
    elif board[2] == char and board[4] == char and board[6] == char:
        return True

    # if above conditions not satisfied
    else:
        return False

# define isFull function
def isFull():
    if board.count(" ") == 0:
        return True
    else:
        return False


# create an empty list with 9 elements
board = [" "] * 9

# calling displayBoard function
displayBoard()

# Get the input from user
p = input("please enter the TOSS : ")

# Create an infinite loop
while True:
    # when user enters x or o
    if p == "TOSS" or p == "toss":
        # calling tossSymbol function
        tos = tossSymbol()

        # if the random number is 1, p1 is winner
        if tos == 1:
            p1 = "x"
            p2 = "o"

        elif tos == 0:
            p2 = "x"
            p1 = "o"
        break

    # when user enters other than x or o
    else:
        print("Enter the value again ")
        p = input("please enter the TOSS again: ")
        continue

# display the symbols for users
print("P1 allocated symbol is", p1)
print("P2 allocated symbol is", p2)

# Start an infinite loop to run game continuously
while True:

    # Start an infinite loop to get input from users
    while True:
        # Get input from user1
        play1 = int(input("Player 1 Enter the position between 1 to 9: "))
        # verify the board is empty for the entered position
        if board[play1] == " ":
            board[play1] = p1
            break
        else:
            print("position is already taken")

    # calling display board function to see the output
    displayBoard()

    # calling isWinner function to find whether player1 has won or not
    if isWinner(p1):
        print("Player 1 has won")
        break

    # calling isFull function check whether all blocks are full
    if isFull():
        print("Match Tied !")
        break

    while True:
        # Get input from user1
        play2 = int(input("Player 2 Enter the position between 1 to 9: "))
        # verify the board is empty for the entered position
        if board[play2] == " ":
            board[play2] = p2
            break
        else:
            print("position is already taken")

    # calling display board function to see the output
    displayBoard()

    # calling isWinner function to find whether player1 has won or not
    if isWinner(p2):
        print("Player 2 has won")
        break
    # calling isFull function check whether all blocks are full
    if isFull():
        print("Match Tied !")
        break