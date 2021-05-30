ticboard = {1: ' ', 2: ' ', 3: ' ',
           4: ' ', 5: ' ', 6: ' ',
           7: ' ', 8: ' ', 9: ' '}#I will use 'x' for human and 'o' for computer no matter who starts the game, return 1 for true, 2 for false
def display(ticboard):#prints the tictactoe board
    print(ticboard[1] + '|' + ticboard[2] + '|' + ticboard[3])
    print('-+-+-')
    print(ticboard[4] + '|' +ticboard[5] + '|' + ticboard[6])
    print('-+-+-')
    print(ticboard[7] + '|' + ticboard[8] + '|' + ticboard[9])
    print("\n")
def move_human():#move by human
    step=int(input("Enter the postion for your next move "))
    move('X',step)
    return 
def validity(pos):# checks if the move is allowed
    if ticboard[pos]==' ':
        return 1
    else :
        return 0
def stalemate():#checks for draw
    for key in [ticboard.keys()]:
        if ticboard[key]==' ':
          return 0
    return 1

def unbiastvict():#checks for basic victory in tic tac toe
    #first columnwise , then rowwise and then diagonally
    if (ticboard[1]==ticboard[4] and ticboard[7]==ticboard[4] and ticboard [1]!=' '):
        return 1
    elif (ticboard[2]==ticboard[5] and ticboard[8]==ticboard[5] and ticboard [2]!=' '):
        return 1
    elif(ticboard[3]==ticboard[6] and ticboard[9]==ticboard[6] and ticboard [3]!=' '):
        return 1
    elif(ticboard[1]==ticboard[2] and  ticboard[2]==ticboard[3] and ticboard [1]!=' '):
        return 1
    elif(ticboard[4]==ticboard[5] and ticboard[5]==ticboard[6] and ticboard [4]!=' '):
        return 1
    elif(ticboard[7]==ticboard[8] and ticboard[8]==ticboard[9] and ticboard [7]!=' '):
        return 1
    elif(ticboard[1]==ticboard[5] and ticboard[5]==ticboard[9] and ticboard [1]!=' '):
        return 1
    elif(ticboard[3]==ticboard[5] and ticboard[5]==ticboard[7] and ticboard [5]!=' '):
        return 1
    else :
        return 0
def move(team,pos):#allows for a move
    if validity (pos)==0 :
        #raise ValueError('The position is already filled, please try in another position')
        print('The position is already filled, please try in another position')
        newpos=int(input("Enter the new position here"))
        move(team,newpos)
        return 
    else :
        ticboard[pos]=team
        display(ticboard)
        if stalemate()==1:
            print ("DRAW!")
            exit()
        if team_vict('X')==1:
            print ("Human wins !")
            exit()
        elif team_vict('O')==1:
            print ("Bot Wins!")
            exit()
        return
def team_vict(team):#checks if a particular team has won
    if (ticboard[1]==ticboard[4] and ticboard[7]==ticboard[4] and ticboard [4]==team):
         return 1
    elif (ticboard[2]==ticboard[5] and ticboard[8]==ticboard[5] and ticboard [8]==team):
        return 1
    elif(ticboard[3]==ticboard[6] and ticboard[9]==ticboard[6] and ticboard [3]!=team):
        return 1
    elif(ticboard[1]==ticboard[2] and ticboard[2]==ticboard[3] and ticboard [2]!=team):
        return 1
    elif(ticboard[4]==ticboard[5] and ticboard[5]==ticboard[6] and ticboard [4]!=team):
        return 1
    elif(ticboard[7]==ticboard[8] and ticboard[8]==ticboard[9] and ticboard [8]!=team):
        return 1
    elif(ticboard[1]==ticboard[5] and ticboard[5]==ticboard[9] and ticboard [5]!=team):
        return 1
    elif(ticboard[3]==ticboard[5] and ticboard[5]==ticboard[7] and ticboard [5]!=team):
        return 1
    else :
        return 0 
def move_computer():#move by comp
    highscore=-999
    favourablemove=0
    for key in [ticboard.keys()]:
        if (validity(key)==1):
            ticboard[key]='O'
            scoreindex=minmax(ticboard,0)
            ticboard[key]=' ' 
            if highscore < scoreindex:
                highscore=scoreindex
                favourablemove=key
    move('O',favourablemove)
    return
def minmax(ticboard,Maximiser):
    if stalemate()==1:
         return 0
    elif team_vict('X')==1:
        return -1
    elif team_vict('O')==1:
        return 1
    if (Maximiser==1):
        highscore=-999
        for key in [ticboard.keys()]:
            if (validity(key)==1):
                ticboard[key]='O'
                scoreindex=minmax(ticboard,0)
                ticboard[key]=' '  
                if (highscore<scoreindex):
                    highscore=scoreindex
        return highscore
    else :
        lowscore=999
        for key in [ticboard.keys()]:
            if (validity(key)==1):
                ticboard[key]='X'
                scoreindex=minmax(ticboard,1)
                ticboard[key]=' '  
                if (lowscore>scoreindex):
                    lowscore=scoreindex
        return lowscore
display(ticboard)
global firstComputerMove
firstComputerMove = True
print("The positions are : in left to right order ,For the first row 1,2,3 ; for the second row 4,5,6 ; for the third row 7,8,9")
while unbiastvict !=1:
     move_computer()
     move_human()


     

