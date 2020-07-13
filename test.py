import random
import re


def first_printing():
    print('Here is the positions\n')
    print('  1  |  2  |  3\n_ _ _ _ _ _ _ _ _\n  4  |  5  |  6\n_ _ _ _ _ _ _ _ _\n  7  |  8  |  9\n')


def print_board(user, computer):
    board = '  1  |  2  |  3\n_ _ _ _ _ _ _ _ _\n  4  |  5  |  6\n_ _ _ _ _ _ _ _ _\n  7  |  8  |  9\n'
    temp1 = ''
    temp2 = ''
    for i in user:
        temp1 = temp1 + str(i)
    for i in computer:
        temp2 = temp2 + str(i)
    board = re.sub('['+temp1+']', 'O', board)
    board = re.sub('['+temp2+']', 'X', board)
    print(board)
    return board


def user_input(user_list, computer_list):
    check1 = False
    check2 = False
    final = False
    pos = input('enter you position here:')
    while not final:
        if isinstance(pos, int) and 0 < pos < 10:
            check1 = True
        else:
            check1 = False
            pos = input('Please enter an integer from 1 to 9:')
            continue

        if pos in user_list or pos in computer_list:
            pos = input('Move has already been played:')
            continue
        else:
            check2 = True

        if check1 and check2:
            return pos


def check_win(player):
    """
    :param player:
    :return: boolean that is True if player has won
    """
    win = False
    if 5 in player:
        if (4 in player and 6 in player) or \
           (1 in player and 9 in player) or \
           (2 in player and 8 in player) or \
           (3 in player and 7 in player):
            win = True
    if (1 in player and 2 in player and 3 in player) or \
       (1 in player and 4 in player and 7 in player) or \
       (7 in player and 8 in player and 9 in player) or \
       (3 in player and 6 in player and 9 in player):
        win = True
    return win


def game():
    user = []
    computer = []
    computer_options = [1,2,3,4,5,6,7,8,9]
    finish = False
    first_printing()
    while not finish:
        a = user_input(user, computer)
        user.append(a)
        print('You have played ' +str(a))
        if check_win(user):
            print_board(user, computer)
            print("You win!")
            finish = True
            continue
        computer_options.remove(a)
        if len(computer_options) == 0:
            print("It's a draw")
            finish = True
            continue
        b = random.choice(computer_options)
        computer.append(b)
        computer_options.remove(b)
        print('Your opponent plays ' +str(b))
        print_board(user, computer)
        if check_win(computer):
            print("You suck!")
            finish = True
            continue


game()
