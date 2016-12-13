

import connectfour
import connectfour_board

def main():
    '''Starts the game and handles the taking of turns until the
    game is over.'''
    connectfour_board.rules()
    current_board = connectfour.new_game()
    
    while connectfour.winner(current_board) == connectfour.NONE:

        try:
            turn = connectfour_board.get_turn(current_board)
            print('''IT'S YOUR TURN, {} \n'''.format(turn))
            connectfour_board.print_current_board(current_board)
            
            current_board = user_input(current_board)
        except:
            print ('ERROR, TRY AGAIN!!!')
    
    else:

        if connectfour.winner(current_board) == connectfour.RED:
            connectfour_board.print_current_board(current_board)
            print("RED WINS!!")
        elif connectfour.winner(current_board) == connectfour.YELLOW:  
            connectfour_board.print_current_board(current_board)
            print("YELLOW WINS!!")
            
        


    

def user_input(game_state)-> connectfour.GameState:
    '''Takes in the player's input as a move and plays accordingly.'''
    move = input().strip(' ')

    if move.upper().split()[0] == 'POP':
        return connectfour.pop(game_state, int(move[-1])-1
                               )

    elif move.upper().split()[0] == 'DROP':
        return connectfour.drop(game_state, int(move[-1])-1)
    else:
        raise connectfour.InvalidMoveError



if __name__ == '__main__':
    main()
         
    
