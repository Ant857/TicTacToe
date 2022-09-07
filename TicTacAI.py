#Here BOARD could also be declared as list of list
#In that manner you could easily use notation BOARD[x][y] or BOARD[y][x]

BOARD = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

import random
import math

def print_board(BOARD):
    print(BOARD[1]+'|'+BOARD[2]+'|'+BOARD[3])
    print("-+-+-")
    print(BOARD[4]+'|'+BOARD[5]+'|'+BOARD[6])
    print("-+-+-")
    print(BOARD[7]+'|'+BOARD[8]+'|'+BOARD[9])

def take_turnAIDumb():
    random_space = random.randrange(1,9)
    while BOARD[random_space] != ' ':
        random_space = random.randrange(1,9)
    BOARD[random_space] = 'O'
    print("AI Makes His Move")


#MINIMAX TERMINAL FUNCTION
def minimax(board, depth, isMaximizing):
    if check_for_win(BOARD) != False:
        if check_for_win(BOARD) == 'X':
            return -10
        elif check_for_win(BOARD) == 'O':
            return 10
        elif check_for_win(BOARD) == "Nobody":
            return 0
    if isMaximizing:
        best_score = -math.inf
        for i in range(1, 10):
            if BOARD[i] == ' ':
                BOARD[i] = 'O'
                score = minimax(BOARD, depth + 1, False)
                BOARD[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if BOARD[i] == ' ':
                BOARD[i] = 'X'
                score = minimax(BOARD, depth + 1, True)
                BOARD[i] = ' '
                best_score = min(score, best_score)
        return best_score

#iterate through all moves looking for best move
def take_turnAISmart():
    best_score = -math.inf
    for i in range(1, 10):
        if BOARD[i] == ' ':
            BOARD[i] = 'O'
            score = minimax(BOARD, 0, False)
            BOARD[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    BOARD[best_move] = 'O'
    print("AI Makes His Move")

def take_turn(player):
    move = int(input("Player " + str(player) + "s Turn: "))
    while BOARD[move] != ' ' or move < 1 or move > 9:
        if BOARD[move] != ' ':
            print("Space Already Taken")
        else:
            print("Number must be between 1 and 9")
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
    draw = True
    for i in range(1,10):
        if BOARD[i] == ' ':
            draw = False
    if draw == True:
        return "Nobody"
    return False
        

def main():
    players = int(input("1 or 2 Players"))
    while players != 1 and players != 2:
        print("Please Choose 1 or 2")
        players = int(input("1 or 2 Players"))
    game_over = False
    turn = 1
    print_board(BOARD)
    while game_over == False :
        if players == 1:
            take_turn(1)
            print_board(BOARD)

            if check_for_win(BOARD) != False:
                print(check_for_win(BOARD) + " Wins")
                game_over = True
                break
        
            take_turnAISmart()
        else:
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


