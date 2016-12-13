
import socket
from collections import namedtuple


connection = namedtuple('connection', ['connectfour_socket', 'connectfour_in', 'connectfour_out'])


def user_interface():
    host = read_host()
    port = read_port()

    connection = connector(host, port)

def read_host() -> str:                        
    while True:
                        
        host = input('Please enter a host: ').strip(' ')

        if len(host) == 0:
            print('''Please specify a valid host''')

        elif host != 'woodhouse.ics.uci.edu':
            print(''' Sorry, please enter the correct host.''')

        else:
            return host

def read_port() -> int:
    while True:
        try:
            port = int(input('Please enter the Port number: ').strip(' '))

            if port != 4444:
                print('Sorry, invalid port. Try again!')

            else:
                return port

        except ValueError:
            print('Sorry, ports must be a positive integer.')


def connector(host: str, port: int) -> 'connection':
    #get the host by calling read_host()
    #get port by callin read_port()

    connectfour_socket = socket.socket()
        
    print('Connecting to the server :)')
    connectfour_socket.connect((host, port))
    print('Connection was successful!')

    username = (input('Please enter a username: '))
    
    connectfour_in = connectfour_socket.makefile('r')
    connectfour_out = connectfour_socket.makefile('w')
    

    connectfour_out.write('I32CFSP_HELLO ' + username + '\n')                       
    connectfour_out.flush()
    print(connectfour_in.readlines()[:-1])

    connectfour_out.write('AI_GAME' + '\n')
    connectfour_out.flush()
    print(connectfour_in.readline()[:-1])
      
    return connectfour_socket, connectfour_in, connectfour_out

def client_move(connection: 'connection', move: list):
    connectfour_socket, connectfour_in, connectfour_out = connection

    send = ''
    

    if move[0].upper() == 'DROP' or 'POP':
        send = (move[0].upper() + ' ' + move[1] + '\r\n')
        connectfour_out.write(send)
        connectfour_out.flush()
    else:
        print('Error')

def server_move(connection: 'connection') -> list:
    connectfour_socket, connectfour_in, connectfour_out = connection
    receive = connectfour_in.readline().split()
    return receive
    

def close(connection: 'connection') -> None:
    connectfour_socket, connectfour_in, connectfour_out = connection
    connectfour_in.close()
    connectfour_out.close()
    connectfour_socket.close()
    print('Connection Closed!')




