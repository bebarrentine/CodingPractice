from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input(player_choice):
    global player_choice1

    player_choice1 = 't'

    while player_choice1 not in ['X', 'O']:
        player_choice1 = input('Choose your marker! (X or O): ')

    print('Your marker is {}!'.format(player_choice1))


board = ['#', '', '', '', '', '', '', '', '', '']


def place_marker(board, marker, position):
    position_choice = 'a'
    if player_choice1 == 'X':
        marker = 'O'
    else:
        marker = 'X'
    while position_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position_choice = input('Other player\'s turn! Choose a position (1-9): ')
        if position_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position_choice = input('Other player\'s turn! Choose a position (1-9): ')
        else:
            pass

    position = int(position_choice)

    if space_check(board, position) == True:
        board[position] = marker
        return display_board(board)
    else:
        print('Sorry, that space is taken! You lost your turn.')


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    elif board[8] == board[5] == board[2] == mark:
        return True
    elif board[9] == board[6] == board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    else:
        return False

def choose_first():
    global x

    x = random.randint(1, 2)

    return x

def space_check(board, position):
    if position in range(1,10):
        if board[position] == 'X':
            return False
        elif board[position] == 'O':
            return False
        else:
            return True

def full_board_check(board):
    if '' in board:
        return False
    else:
        return True


def player_choice(board, marker):
    next_player_choice = 'b'
    if player_choice1 == 'X':
        marker = 'X'
    else:
        marker = 'O'
    while next_player_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        next_player_choice = input('Player {}, choose a position on the board! (1-9):'.format(x))
        if next_player_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            next_player_choice = input('Player {}, choose a position on the board! (1-9):'.format(x))
        else:
            pass

    next_position = int(next_player_choice)

    if space_check(board, next_position) == True:
        board[next_position] = marker
        return display_board(board)
    else:
        print('Sorry, that space is taken! You lost your turn.')


def replay():
    replay_question = 'c'

    while replay_question not in ['Y', 'N']:
        replay_question = input('Would you like to play again? (Y or N): ')

    if replay_question == 'Y':
        return True
    else:
        return False

# GAME STARTS HERE

print('Welcome to Tic Tac Toe!')

if choose_first() == 1:
    print('Player 1 moves first!')
    player_input('t')
elif choose_first() == 2:
    print('Player 2 moves first!')
    player_input('t')

while True:

    if win_check(board, 'X') == True:
        print('X has won!')
        break
    else:
        pass

    if win_check(board, 'O') == True:
        print('O has won!')
        break
    else:
        pass

    if full_board_check(board) == False:
        pass
    else:
        print('The board is full! The game has ended.')
        break

    player_choice(board, player_choice1)

    if win_check(board, 'X') == True:
        print('X has won!')
        break
    else:
        pass

    if win_check(board, 'O') == True:
        print('O has won!')
        break
    else:
        pass

    if full_board_check(board) == False:
        pass
    else:
        print('The board is full! The game has ended.')
        break

    place_marker(board, player_choice1, 2)

while replay():

    print('Welcome to Tic Tac Toe!')

    if choose_first() == 1:
        print('Player 1 moves first!')
        player_input('t')
    elif choose_first() == 2:
        print('Player 2 moves first!')
        player_input('t')

    board = ['#', '', '', '', '', '', '', '', '', '']

    while True:

        if win_check(board, 'X') == True:
            print('X has won!')
            break
        else:
            pass

        if win_check(board, 'O') == True:
            print('O has won!')
            break
        else:
            pass

        if full_board_check(board) == False:
            pass
        else:
            print('The board is full! The game has ended.')
            break

        player_choice(board, player_choice1)

        if win_check(board, 'X') == True:
            print('X has won!')
            break
        else:
            pass

        if win_check(board, 'O') == True:
            print('O has won!')
            break
        else:
            pass

        if full_board_check(board) == False:
            pass
        else:
            print('The board is full! The game has ended.')
            break

        place_marker(board, player_choice1, 2)

else:
    print('Thanks for playing!')
    board = ['#', '', '', '', '', '', '', '', '', '']
