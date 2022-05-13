import os # Used to clean screen
#os.system('color')

def is_float_digit(n: str) -> bool:
    try:
        float(n)
        return True
    except ValueError:
        return False

# Class stack (for each column)
class column_stack:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)
    def push(self, piece):
        maxRow = 6
        if len(self._list) <= maxRow:
            self._list.append(piece)
        else:
            return 0
    def peek(self):
        return self._list[-1]

# Initialize board (empty)
def drawBoard():
    # empty board
    #rows = ['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5', 'Row 6']
    board = []
    for k in range(0, 6):
        board.append([' '] * 7)
    return board

# Initialize Stacks (empty)
def initialStacks():
    stackList = []
    for i in range (7): stackList.append(column_stack())
    column_stack()
    return stackList


# print board
def printBoard(board):
    os.system("clear")
    row = [[n] for n in range(6)]
    lenRows = 6
    for I in range (lenRows): row[I][0] = 'Row' + ' ' + str(lenRows-I) + ': | '
    print("-------------------------------------")
    for k in range(lenRows):
        for J in range(1, 8, 1):
            row[k][0] = row[k][0] + str(board[k][J - 1])  + ' | '
        print(row[k][0])
        print("-------------------------------------")
    print('        C1  C2  C3  C4  C5  C6  C7')

# Move
def move(piece, board, Stacks, player):
    acceptedColumnNumber = ['1', '2', '3', '4', '5', '6', '7']
    if piece == player:
        pos = str(input('Your move: '))
        if (pos not in acceptedColumnNumber) == True:
            print('Input must be positive integer between 1 and 7')
            move(piece, board, Stacks, player)
        else:
            pos = int(pos)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                print('Column is full, try other columns again...')
                move(piece, board, Stacks, player)
    else:
        pos = str(input('Your move: '))
        if (pos not in acceptedColumnNumber) == True:
            print('Input must be positive integer between 1 and 7')
            move(piece, board, Stacks, player)
        else:
            pos = int(pos)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                print('Column is full, try other columns again...')
                move(piece, board, Stacks, player)
    return board, Stacks


# Check wins
def checkWin(S, board):
    game = False
    # Horizontal checker
    for r in range(0, 6):
        for c in range(3, 7):
            if (board[r][c] == board[r][c - 1] == \
                    board[r][c - 2] == board[r][c - 3] == S):
                game = True
            else:
                continue
    # Vertical checker
    for c in range(0, 7):
        for r in range(3, 6):
            if (board[r][c] == board[r - 1][c] == \
                    board[r - 2][c] == board[r - 3][c] == S):
                game = True
            else:
                continue
    # Diagonal checker
    for c in range(0, 4):
        for r in range(0, 3):
            if (board[r][c] == board[r + 1][c + 1] == \
                    board[r + 2][c + 2] == board[r + 3][c + 3] == S or
                    board[r + 3][c] == board[r + 2][c + 1] == \
                    board[r + 1][c + 2] == board[r][c + 3] == S):
                game = True
            else:
                continue
    if game == True:
        print(S + ' wins!')
    return game


# Main program
def main():
    # start game
    print("This is connect four game, you can exit game by pressing control + c, or ", end='')
    startGame = False
    while (startGame == False):
        startInput = input("press y, and then enter key to start the game.\n")
        if startInput == 'y':
            startGame = True
            os.system("clear")
        else:
            os.system("clear")
            if (startInput==''):
                print("You entered an empty.")
            elif (is_float_digit(startInput) == True):
                print("You entered a number instead of y.")
            elif(startInput=='Y'):
                print("You entered Capital Y, please try again.")
            elif (' ' in startInput):
                print("You entered space in your input, please try again.")
            else:
                print("illegal Input.")


    # Prompt player input
    player1 = str(input('please choose X or O: '))
    while player1 != 'X' and player1 != 'O':
         os.system("clear")
         if len(player1) > 1 and ' '  not in player1:
            print("input is more than one char check your input and try again")
         if len(player1) == 0:
            print("Your input is null, please try again")
         if player1.isalpha() == False and player1 != "" and player1 != '0' and ' '  not in player1:
            print("Your input is not alphabets try again")
         if player1 == 'x':
             print("you entered lowercase x, please enter capital X.")
         if player1 == 'o':
             print("you entered lowercase o, please enter capital O.")
         if player1 == '0':
             print("you entered zero number (0), please enter capital O. They are just similar :)")
         if ' ' in player1 and player1 != ' ':
             print("Your input has extra space please check your input.")
         if player1 == ' ':
             print("You entered just space.")
         player1 = str(input('Illegal input, please again choose X or O: '))
    else:
        player2 = 'X' if player1 == 'O' else 'O'


    # Print board
    board = drawBoard()
    Stacks = initialStacks()
    printBoard(board)
    print('In order to play the game, please enter a positive integer number between 1 and 7 for each column on the board. '
          'The first person to stack four pieces horizontally, vertically, or diagonally wins:)')
    game = False
    moveCount = 0 # To check all stacks a
    while game == False:
        # X player
        board, Stacks = move('X', board, Stacks, player1)
        printBoard(board)
        game = checkWin('X', board)
        moveCount += 1
        if game == True:
            break
        # O player
        board, Stacks = move('O', board, Stacks, player2)
        printBoard(board)
        game = checkWin('O', board)
        moveCount += 1
        if game == True:
            break
        if moveCount == 42 and game == False:
            print("Both of you were very good. The game equalised. No win !")
            break
    print('Good game:)')


if __name__ == '__main__':
    main()