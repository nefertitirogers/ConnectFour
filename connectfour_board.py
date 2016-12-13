
import connectfour

def print_current_board(game_state):
    '''Prints the current board'''
    board = game_state.board 
    print('1 2 3 4 5 6 7 ')
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if board[col][row] == 0:
                print('.', end = ' ')
            elif board[col][row] == 1:
                print('R', end = ' ')
            elif board[col][row] == 2:
                print('Y', end = ' ')
        print()
                
def get_turn(game_state):
    '''Converts the turn inside the namedtuple into a string
    representing the player's color'''
    turn = game_state.turn
    if turn == 1:
        return 'RED'
    elif turn == 2:
        return 'YELLOW'

def rules () -> str:
    '''Prints the rules for the players.''' 
    print ("Welcome to Connect Four!")
    print ('\n')
    print ('''We will be playing the game with red and yellow pieces. Red always goes first.''')
    print ('''When it's your turn you can either 'POP' or 'DROP' a piece into a column''')
    print ('''To drop a piece enter 'DROP' followed by the column number (1-7).''')
    print ('''To pop a piece enter 'POP' followed by the column number(1-7).''')
    print ('''Your input should look something like: 'POP 6' or 'DROP 4' ''')
    print ('''First player to get four pieces in a row wins!''')
    print('\n')
