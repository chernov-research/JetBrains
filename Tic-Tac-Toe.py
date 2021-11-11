# Project: Simple Tic-Tac-Toe
import sys

data = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

data_1D = []


def grid():
    print('---------')
    print('|', data[0][0], data[0][1], data[0][2], '|')
    print('|', data[1][0], data[1][1], data[1][2], '|')
    print('|', data[2][0], data[2][1], data[2][2], '|')
    print('---------')


# Printing an empty grid
grid()


# Player 1 turn
def player_1():
    x_y = input('Enter the coordinates: ').split()
    min_num = 1
    max_num = 3
    try:
        x = int(x_y[0])
        y = int(x_y[1])
        if min_num <= x <= max_num and min_num <= y <= max_num:
            if data[x - 1][y - 1] == 'X' or data[x - 1][y - 1] == 'O':
                print('This cell is occupied! Choose another one!')
                player_1()
            else:
                data[x - 1][y - 1] = 'X'
                grid()
                win_check()
                player_2()
        else:
            print('Coordinates should be from 1 to 3!')
            player_1()
    except ValueError:
        print('You should enter numbers!')
        player_1()


# Player 2 turn
def player_2():
    x_y = input('Enter the coordinates: ').split()
    min_num = 1
    max_num = 3
    try:
        x = int(x_y[0])
        y = int(x_y[1])
        if min_num <= x <= max_num and min_num <= y <= max_num:
            if data[x - 1][y - 1] == 'X' or data[x - 1][y - 1] == 'O':
                print('This cell is occupied! Choose another one!')
                player_2()
            else:
                data[x - 1][y - 1] = 'O'
                grid()
                win_check()
                player_1()
        else:
            print('Coordinates should be from 1 to 3!')
            player_2()
    except ValueError:
        print('You should enter numbers!')
        player_2()


def win_check():
    wins = [[data[0][0], data[0][1], data[0][2]],
            [data[1][0], data[1][1], data[1][2]],
            [data[2][0], data[2][1], data[2][2]],
            [data[0][0], data[1][0], data[2][0]],
            [data[0][1], data[1][1], data[2][1]],
            [data[0][2], data[1][2], data[2][2]],
            [data[0][0], data[1][1], data[2][2]],
            [data[0][2], data[1][1], data[2][0]]]

    data_1D.clear()
    for i in range(len(data)):
        for j in range(len(data)):
            data_1D.append(data[i][j])
    print(data_1D)
    if ['X', 'X', 'X'] in wins:
        print('X wins')
        sys.exit()
    elif ['O', 'O', 'O'] in wins:
        print('O wins')
        sys.exit()
    elif ' ' not in data_1D:
        print('Draw')
        sys.exit()

player_1()
