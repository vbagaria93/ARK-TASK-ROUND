# Make a copy of this file
# and Add a class called AI Agent 
import sys
import numpy as np
import random
"""
   I was planning to use q value learning and pytorch but I could not 
   comprehend the logic completely, thats why I skipped it, A sample code and all 
   my research regarding it can be found in my Github repo
"""
from gym_tictactoe.envs.tictactoe_env import TicTacToeEnv, after_action_state, check_game_status, agent_by_mark
from numpy.core.defchararray import swapcase
from numpy.core.numeric import array_equal

class HumanAgent(object):
    def __init__(self, mark):
        self.mark = mark

    def act(self, ava_actions,reward):
        while True:
            uloc = input("Enter location[000 - 222], q for quit: ")
            if uloc.lower() == 'q':
                return None
            try:
                action = uloc
                if action not in ava_actions:
                    raise ValueError()
            except ValueError:
                print("Illegal location: '{}'".format(uloc))
            else:
                break

        return self.mark + action
class AIAgent(object):
    def __init__(self, mark):
        self.mark = mark
    def act(self,ava_actions,reward):
         """
     convert reward to a linear array in the form of bcr
         """
         l=np.zeros(27,dtype='uint8')
         o=0
         reward=np.transpose(reward,[0,1,2])
         for i in range (0,3):
             for j in range (0,3):
                 for k in range (0,3):
                     l[o]=reward[i][j][k]
                     o+=1
         reward=l
         rew=np.zeros(27,dtype='uint8')
         for i in range (0,27,3):#checking column wise
             """
               If there are two occurences of the opponent player in a row, column, diagonal ,vertex, it will be prioritized and blocking the opponent 
               would be prioritized over prospecting the move for ourselves, except when the move is a winning one, then we will check 
               for one occurence at a time and keep on adding a particular reward for a place according to the dynamics of the game, thereby 
               carrying out an exhaustive search of the game space
             """
             if (reward[i]==reward[i+1] and reward[i+2] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+2] += 98
                 else :
                     rew [i+2] += 196
             elif (reward[i]==reward[i+2] and reward[i+1]==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+1]+=98
                 else :
                     rew[i+1]+=196
             elif (reward[i+1]==reward[i+2] and reward[i] ==0 and reward[i+2]!=0) :
                 if reward[i+1]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+1]==reward[i+2] and reward[i+1]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+1]+=50
                     rew[i+2]+=50
                 else:
                     rew[i+1]+=49
                     rew[i+2]+=49
             elif (reward[i+1]==reward[i] and reward[i+1]==0 and reward [i+2]!=0):
                 if reward [i+2]=='o':
                     rew[i+1]+=50
                     rew[i]+=50
                 else:
                     rew[i+1]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+2] and reward[i]==0 and reward [i+1]!=0):
                 if reward [i+1]=='o':
                     rew[i]+=50
                     rew[i+2]+=50
                 else:
                     rew[i]+=49
                     rew[i+2]+=49
             else :
                 for j in range (i,i+3):
                     rew[j]+=1
         k=0
         while k<20:  #columnwise
             """
                    Exhaustive search of the row space like we did for the row case 
             """
             for i in range (k,k+3):
                 
                  if (reward[i]==reward[i+3] and reward[i+6] ==0 and reward[i]!=0) :
                      if reward[i]=='o':
                          rew [i+6]+=98
                      else :
                          rew [i+6]+=196
                  elif (reward[i]==reward[i+6] and reward[i+3] ==0 and reward[i]!=0) :
                      if reward[i]=='o':
                          rew [i+3]+=98
                      else :
                          rew[i+3]+=196
                  elif (reward[i+3]==reward[i+6] and reward[i] ==0 and reward[i+6]!=0) :
                      if reward[i+3]=='o':
                          rew [i]+=98
                      else :
                          rew[i]+=196
                  elif (reward[i+3]==reward[i+6] and reward[i+3]==0 and reward [i]!=0):
                      if reward [i]=='o':
                          rew[i+3]+=50
                          rew[i+6]+=50
                      else:
                          rew[i+3]+=49
                          rew[i+6]+=49
                  elif (reward[i+3]==reward[i] and reward[i+3]==0 and reward [i+6]!=0):
                      if reward [i+6]=='o':
                          rew[i+3]+=50
                          rew[i]+=50
                      else:
                          rew[i+3]+=49
                          rew[i]+=49
                  elif (reward[i]==reward[i+6] and reward[i]==0 and reward [i+3]!=0):
                      if reward [i+3]=='o':
                          rew[i]+=50
                          rew[i+6]+=50
                      else:
                          rew[i]+=49
                          rew[i+6]+=49
                  else :
                          rew[i]+=1
                          rew[i+3]+=1
                          rew[i+6]+=1
             k+=9
         for i in range (0,9):
             """
             Checking along the vertices (3 dimensional, one in each block)
             """
             if (reward[i]==reward[i+9] and reward[i+18] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+18]+=98
                 else :
                     rew [i+18]+=196
             elif (reward[i]==reward[i+18] and reward[i+9] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+9]+=98
                 else :
                     rew[i+9]+=196
             elif (reward[i+9]==reward[i+18] and reward[i] ==0 and reward[i+18]!=0) :
                 if reward[i+9]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+9]==reward[i+18] and reward[i+9]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+9]+=50
                     rew[i+18]+=50
                 else: 
                     rew[i+9]+=49
                     rew[i+18]+=49
             elif (reward[i+9]==reward[i] and reward[i+9]==0 and reward [i+18]!=0):
                 if reward [i+18]=='o':
                     rew[i+9]+=50
                     rew[i]+=50
                 else:
                     rew[i+9]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+18] and reward[i]==0 and reward [i+9]!=0):
                 if reward [i+9]=='o':
                     rew[i]+=50
                     rew[i+18]+=50
                 else:
                     rew[i]+=49
                     rew[i+18]+=49
             else :
                 rew[i]+=1
                 rew[i+9]+=1
                 rew[i+18]+=1
         """
         checking along the face diagonals
         1. Prinicipal Diagonal
         """
         i=0
         while i < 20:
             if (reward[i]==reward[i+4] and reward[i+8] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+8]+=98
                 else :
                     rew [i+8]+=196
             elif (reward[i]==reward[i+8] and reward[i+4] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+4]+=98
                 else :
                     rew[i+4]+=196
             elif (reward[i+4]==reward[i+8] and reward[i] ==0 and reward[i+8]!=0) :
                 if reward[i+4]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+4]==reward[i+8] and reward[i+4]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+4]+=50
                     rew[i+8]+=50
                 else:
                     rew[i+4]+=49
                     rew[i+8]+=49
             elif (reward[i+4]==reward[i] and reward[i+4]==0 and reward [i+8]!=0):
                 if reward [i+8]=='o':
                     rew[i+4]+=50
                     rew[i]+=50
                 else:
                     rew[i+4]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+8] and reward[i]==0 and reward [i+4]!=0):
                 if reward [i+4]=='o':
                     rew[i]+=50
                     rew[i+8]+=50
                 else:
                     rew[i]+=49
                     rew[i+8]+=49
             else :
                     rew[i+4]+=1
                     rew[i+8]+=1
                     rew[i]+=1
             i+=9
         i=2
         while i<21:
             """
             2. Right Diagonal
             """
             if (reward[i]==reward[i+2] and reward[i+4] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+4]+=98
                 else :
                     rew [i+4]+=196
             elif (reward[i]==reward[i+4] and reward[i+2] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+2]+=98
                 else :
                     rew[i+2]+=196
             elif (reward[i+2]==reward[i+4] and reward[i] ==0 and reward[i+4]!=0) :
                 if reward[i+2]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+2]==reward[i+4] and reward[i+2]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+2]+=50
                     rew[i+4]+=50
                 else:
                     rew[i+2]+=49
                     rew[i+4]+=49
             elif (reward[i+2]==reward[i] and reward[i+2]==0 and reward [i+4]!=0):
                 if reward [i+4]=='o':
                     rew[i+2]+=50
                     rew[i]+=50
                 else:
                     rew[i+2]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+4] and reward[i]==0 and reward [i+2]!=0):
                 if reward [i+2]=='o':
                     rew[i]+=50
                     rew[i+4]+=50
                 else:
                     rew[i]+=49
                     rew[i+4]+=49
             else :
                 rew[i]+=1
                 rew[i+2]+=1
                 rew[i+4]+=1
             i+=9
         """ 
            Checking others , including along the body diagonal
         """
         for i in range (0,3):
             if (reward[i]==reward[i+12] and reward[i+24] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+24]+=98
                 else :
                     rew [i+24]+=196
             elif (reward[i]==reward[i+24] and reward[i+12] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+12]+=98
                 else :
                     rew[i+12]+=196
             elif (reward[i+12]==reward[i+24] and reward[i] ==0 and reward[i+24]!=0) :
                 if reward[i+12]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+12]==reward[i+24] and reward[i+12]==0 and reward [i]!=0):
                 if reward[i]=='o':
                     rew[i+12]+=50
                     rew[i+24]+=50
                 else:
                     rew[i+12]+=49
                     rew[i+24]+=49
             elif (reward[i+12]==reward[i] and reward[i+12]==0 and reward [i+24]!=0):
                 if reward [i+24]=='o':
                     rew[i+12]+=50
                     rew[i]+=50
                 else:
                     rew[i+12]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+24] and reward[i]==0 and reward [i+12]!=0):
                 if reward [i+12]=='o':
                     rew[i]+=50
                     rew[i+24]+=50
                 else:
                     rew[i]+=49
                     rew[i+24]+=49
             else :
                     rew[i]+=1
                     rew[i+12]+=1
                     rew[i+24]+=1
         i=0
         while (i<7):
             if (reward[i]==reward[i+10] and reward[i+20] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+20]+=98
                 else :
                     rew [i+20]+=196
             elif (reward[i]==reward[i+20] and reward[i+10] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+10]+=98
                 else :
                     rew[i+10]+=196
             elif (reward[i+10]==reward[i+20] and reward[i] ==0 and reward[i+20]!=0) :
                 if reward[i+10]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+10]==reward[i+20] and reward[i+10]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+10]+=50
                     rew[i+20]+=50
                 else:
                     rew[i+10]+=49
                     rew[i+20]+=49
             elif (reward[i+10]==reward[i] and reward[i+10]==0 and reward [i+20]!=0):
                 if reward [i+20]=='o':
                     rew[i+10]+=50
                     rew[i]+=50
                 else:
                     rew[i+10]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+20] and reward[i]==0 and reward [i+10]!=0):
                 if reward [i+10]=='o':
                     rew[i]+=50
                     rew[i+20]+=50
                 else:
                     rew[i]+=49
                     rew[i+20]+=49
             else :
                   rew[i]+=1
                   rew[i+10]+=1
                   rew[i+20]+=1
             i+=3
         """
         Checking the body diagonal
         """
         a=[0,2,6,8]
         b=[26,24,20,18]
         for i in range (0,4):
             if (reward[a[i]]==reward[b[i]] and reward[13] ==0 and reward[a[i]]!=0) :
                 if reward[a[i]]=='o':
                     rew [13]+=98
                 else :
                     rew [13]+=196
             elif (reward[a[i]]==reward[13] and reward[b[i]] ==0 and reward[a[i]]!=0) :
                 if reward[a[i]]=='o':
                     rew [b[i]]+=98
                 else :
                     rew[b[i]]+=196
             elif (reward[b[i]]==reward[13] and reward[a[i]] ==0 and reward[13]!=0) :
                 if reward[b[i]]=='o':
                     rew [a[i]]+=98
                 else :
                     rew[a[i]]+=196
             elif (reward[b[i]]==reward[13] and reward[b[i]]==0 and reward [a[i]]!=0):
                 if reward [a[i]]=='o':
                     rew[b[i]]+=50
                     rew[13]+=50
                 else:
                     rew[b[i]]+=49
                     rew[13]+=49
             elif (reward[b[i]]==reward[a[i]] and reward[b[i]]==0 and reward [13]!=0):
                 if reward [13]=='o':
                     rew[b[i]]+=50
                     rew[a[i]]+=50
                 else:
                     rew[b[i]]+=49
                     rew[a[i]]+=49
             elif (reward[a[i]]==reward[13] and reward[a[i]]==0 and reward [b[i]]!=0):
                 if reward [b[i]]=='o':
                     rew[a[i]]+=50
                     rew[13]+=50
                 else:
                     rew[a[i]]+=49
                     rew[13]+=49
             else :
                 rew[a[i]]+=1
                 rew[b[i]]+=1
                 rew[13]+=1
        
         for i in range (6,9):
             if (reward[i]==reward[i+6] and reward[i+12] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+12]+=98
                 else :
                     rew [i+12]+=196
             elif (reward[i]==reward[i+12] and reward[i+6] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+6]+=98
                 else :
                     rew[i+6]+=196
             elif (reward[i+6]==reward[i+12] and reward[i] ==0 and reward[i+12]!=0) :
                 if reward[i+6]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+6]==reward[i+12] and reward[i+6]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+6]+=50
                     rew[i+12]+=50
                 else:
                     rew[i+6]+=49
                     rew[i+12]+=49
             elif (reward[i+6]==reward[i] and reward[i+6]==0 and reward [i+12]!=0):
                 if reward [i+12]=='o':
                     rew[i+6]+=50
                     rew[i]+=50
                 else:
                     rew[i+6]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+12] and reward[i]==0 and reward [i+6]!=0):
                 if reward [i+6]=='o':
                     rew[i]+=50
                     rew[i+12]+=50
                 else:
                     rew[i]+=49
                     rew[i+12]+=49
             else :
                 rew[i]+=1
                 rew[i+6]+=1
                 rew[i+12]+=1
         for i in range (2,9,3):
             if (reward[i]==reward[i+8] and reward[i+16] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+16]+=98
                 else :
                     rew [i+16]+=196
             elif (reward[i]==reward[i+16] and reward[i+8] ==0 and reward[i]!=0) :
                 if reward[i]=='o':
                     rew [i+8]+=98
                 else :
                     rew[i+8]+=196
             elif (reward[i+8]==reward[i+16] and reward[i] ==0 and reward[i+16]!=0) :
                 if reward[i+8]=='o':
                     rew [i]+=98
                 else :
                     rew[i]+=196
             elif (reward[i+8]==reward[i+16] and reward[i+8]==0 and reward [i]!=0):
                 if reward [i]=='o':
                     rew[i+8]+=50
                     rew[i+16]+=50
                 else:
                     rew[i+8]+=49
                     rew[i+16]+=49
             elif (reward[i+8]==reward[i] and reward[i+8]==0 and reward [i+16]!=0):
                 if reward [i+16]=='o':
                     rew[i+8]+=50
                     rew[i]+=50
                 else:
                     rew[i+8]+=49
                     rew[i]+=49
             elif (reward[i]==reward[i+16] and reward[i]==0 and reward [i+8]!=0):
                 if reward [i+8]=='o':
                     rew[i]+=50
                     rew[i+16]+=50
                 else:
                     rew[i]+=49
                     rew[i+16]+=49
             else :
                 rew[i]+=1
                 rew[i+16]+=1
                 rew[i+8]+=1
         o=0
         matrix=np.zeros((3,3,3),dtype='uint8')
         for i in range (0,3):
             for j in range (0,3):
                 for k in range (0,3):
                     matrix[i][j][k]=rew[o]
                     o+=1
         y1=np.transpose(matrix,(0,2,1))
         ind=np.unravel_index(np.argmax(y1,axis=None),y1.shape)
         l=("{}{}{}".format(ind[0], ind[1], ind[2]))
         return self.mark+l
def play():
    env = TicTacToeEnv()
    print("\n\n\t*******   Welcome to the 3D version of our childhood favorite - TicTacToe  *******\n\t\t\t*******   AI gets to move first *******")
    agents = [AIAgent('1'),HumanAgent('2')]
    episode = 0
    done = False
    reward=np.zeros((3,3,3),dtype='uint8')
    while not done:
        agent = agent_by_mark(agents, str(env.show_turn()))
        print(agent.mark)
        ava_actions = env.available_actions()
        action = agent.act(ava_actions,reward)
        print(action)
        if action is None:
            sys.exit()
        reward, rewar, done, info = env.step(action)
        print()
        env.render()
        if done:
            env.show_result()
            break
    episode += 1
if __name__ == '__main__':
    play()



   
