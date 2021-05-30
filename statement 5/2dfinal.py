import random
human = 'X'  # Player is assigned x while computer is assigned 0
computer = 'O'
print("Positions are as follows, enter an unoccupied digit to proceed and an empty board has been printed. \n 1, 2, 3 \n 4, 5, 6 \n 7, 8, 9 \n")
tictac = {1: ' ', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
          7: ' ', 8: ' ', 9: ' '}
def minimax(tictac, maximiser):#heuristic evaluator, I havent used depth in this function as the number of possible states are very less.
    if (team_vict(computer)):
        return 1
    elif (team_vict(human)):
        return -1
    elif (stalemate()):
        return 0
    if (maximiser):
        extreme = -800
        for key in tictac.keys():
            if (tictac[key] == ' '):
                tictac[key] = computer
                score = minimax(tictac, False)
                tictac[key] = ' '
                if (score > extreme):
                    extreme = score
        return extreme
    else:
        extreme = 800
        for key in tictac.keys():
            if (tictac[key] == ' '):
                tictac[key] = human
                score = minimax(tictac,True)
                tictac[key] = ' '
                if (score < extreme):
                    extreme = score
        return extreme
def empty_space(position):
    if tictac[position] == ' ':
        return True
    else:
        return False
def stalemate():
    for key in tictac.keys():
        if (tictac[key] == ' '):
            return False
    return True
def nextmove(letter, position):
    if empty_space(position):
        tictac[position] = letter
        board(tictac)
        if (stalemate()):
            print("The game ends in a tie")
            exit()
        if win_term():
            if letter == 'O':
                print("Computer wins!")
                exit()
            else:
                print("Human wins!")
                exit()
    else:
        #raise ValueError('Entry restriced as the location is already occupied')
        print("Position is already occupied!")
        position = int(input("Please enter new position which is empty:  "))
        nextmove(letter, position)
def win_term():
    if (tictac[1] == tictac[2] and tictac[1] == tictac[3] and tictac[1] != ' '):
        return True
    elif (tictac[4] == tictac[5] and tictac[4] == tictac[6] and tictac[4] != ' '):
        return True
    elif (tictac[7] == tictac[8] and tictac[7] == tictac[9] and tictac[7] != ' '):
        return True
    elif (tictac[1] == tictac[4] and tictac[1] == tictac[7] and tictac[1] != ' '):
        return True
    elif (tictac[2] == tictac[5] and tictac[2] == tictac[8] and tictac[2] != ' '):
        return True
    elif (tictac[3] == tictac[6] and tictac[3] == tictac[9] and tictac[3] != ' '):
        return True
    elif (tictac[1] == tictac[5] and tictac[1] == tictac[9] and tictac[1] != ' '):
        return True
    elif (tictac[7] == tictac[5] and tictac[7] == tictac[3] and tictac[7] != ' '):
        return True
    else:
        return False
def team_vict(mark):
    if tictac[1] == tictac[2] and tictac[1] == tictac[3] and tictac[1] == mark:
        return True
    elif (tictac[4] == tictac[5] and tictac[4] == tictac[6] and tictac[4] == mark):
        return True
    elif (tictac[7] == tictac[8] and tictac[7] == tictac[9] and tictac[7] == mark):
        return True
    elif (tictac[1] == tictac[4] and tictac[1] == tictac[7] and tictac[1] == mark):
        return True
    elif (tictac[2] == tictac[5] and tictac[2] == tictac[8] and tictac[2] == mark):
        return True
    elif (tictac[3] == tictac[6] and tictac[3] == tictac[9] and tictac[3] == mark):
        return True
    elif (tictac[1] == tictac[5] and tictac[1] == tictac[9] and tictac[1] == mark):
        return True
    elif (tictac[7] == tictac[5] and tictac[7] == tictac[3] and tictac[7] == mark):
        return True
    else:
        return False
def human_():
    position = int(input("Enter the position for 'X':  "))
    nextmove(human, position)
def computer_():
    extreme = -800
    bestMove = 0
    for key in tictac.keys():
        if (tictac[key] == ' '):
            tictac[key] = computer
            score = minimax(tictac,  False)
            tictac[key] = ' '
            if (score > extreme):
                bestMove = key
                extreme = score
    nextmove(computer, bestMove)
def board(tictac):
    print(tictac[1] + '|' + tictac[2] + '|' + tictac[3])
    print('-+-+-')
    print(tictac[4] + '|' + tictac[5] + '|' + tictac[6])
    print('-+-+-')
    print(tictac[7] + '|' + tictac[8] + '|' + tictac[9])
    print("\n")
board(tictac)
o=int(input("Lets have a toss to see who gets to move first, select either 0 or 1 : "))
p=random.randint(0,2)
if(o==p):
     print ("You have won the toss, you go first : ")
     while not win_term():
         human_()
         computer_()
else:
     print("You have lost the toss,AI goes first : ")
     while not win_term():
        computer_()
        human_()
