BOARD = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def print_board(BOARD):
    print(BOARD[1]+'|'+BOARD[2]+'|'+BOARD[3])
    print("-+-+-")
    print(BOARD[4]+'|'+BOARD[5]+'|'+BOARD[6])
    print("-+-+-")
    print(BOARD[7]+'|'+BOARD[8]+'|'+BOARD[9])


def take_turn(player):
    move = int(input("Player " + str(player) + "s Turn: "))
    while BOARD[move] != ' ':
        print("Space Already Taken")
        move = int(input("Player " + str(player) + "s Turn: "))
    if player == 1:
        BOARD[move] = 'X'
    else:
        BOARD[move] = 'O'


def check_for_win(BOARD):
    if (BOARD[1] == BOARD[2] and BOARD[2] == BOARD[3] and BOARD[1] != ' '):
        return BOARD[1]
    if (BOARD[4] == BOARD[5] and BOARD[5] == BOARD[6] and BOARD[4] != ' '):
        return BOARD[4]
    if (BOARD[7] == BOARD[8] and BOARD[8] == BOARD[9] and BOARD[7] != ' '):
        return BOARD[7]
    if (BOARD[1] == BOARD[4] and BOARD[4] == BOARD[7] and BOARD[1] != ' '):
        return BOARD[1]
    if (BOARD[2] == BOARD[5] and BOARD[5] == BOARD[8] and BOARD[2] != ' '):
        return BOARD[2]
    if (BOARD[3] == BOARD[6] and BOARD[6] == BOARD[9] and BOARD[3] != ' '):
        return BOARD[3]
    if (BOARD[1] == BOARD[5] and BOARD[5] == BOARD[9] and BOARD[1] != ' '):
        return BOARD[1]
    if (BOARD[3] == BOARD[5] and BOARD[5] == BOARD[7] and BOARD[3] != ' '):
        return BOARD[3]
    return False
        

def main():
    game_over = False
    turn = 1
    print_board(BOARD)
    while game_over == False:
        if turn == 1:
            take_turn(1)
            turn = 2
        else:
            take_turn(2)
            turn = 1

        print_board(BOARD)
        
        if check_for_win(BOARD) != False:
            print(check_for_win(BOARD) + " Wins")
            game_over = True


main()


