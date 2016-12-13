
import connectfour
import connectfoursocket
import connectfour_board

def main():
    ''''Starts a network game and handles the interpreting of turns until the
    game is over.'''
    connection = connectfoursocket.user_interface()
    connectfour_board.rules()
    network_board = connectfour.new_game()

    while connectfour.winner(network_board) == connectfour.NONE:
        try:
            turn = connectfour_board.get_turn(network_board)
            if turn == 'RED':
                network_board = user_input(network_board)
            elif turn == 'YELLOW':
                network_board = server_input(network_board)
            
        else:

            if connectfour.winner(current_board) == connectfour.RED:
                connectfour_board.print_current_board(current_board)
                print("RED WINS!!")
            elif connectfour.winner(current_board) == connectfour.YELLOW:  
                connectfour_board.print_current_board(current_board)
                print("YELLOW WINS!!")



def user_input(game_state)-> connectfour.GameState:
    #made for the console players
    '''Takes in the player's input as a move and plays accordingly.'''
    move = input().strip(' ')

    if move.upper().split()[0] == 'POP':
        return connectfour.pop(game_state, int(move[-1])-1)
        connectfourconsole.client_move(connection, move.split(' '))

    elif move.upper().split()[0] == 'DROP':
        return connectfour.drop(game_state, int(move[-1])-1)
        connectfourconsole.client_move(connection, move.split(' ')
                                       
    else:
        raise connectfour.InvalidMoveError


def server_input(game_state) -> connectfour.GameState:
        #made for server
        move = connectfoursocket.server_move(game_state)

        if move.upper().split()[0] == 'POP':
            return connectfour.pop(game_state, int(move[-1])-1)

        elif move.upper().split()[0] == 'DROP':
            return connectfour.drop(game_state, int(move[-1])-1)
                                    



















if __name__ == '__main__':
    main()
