
# coding: utf-8
# a simple model of Seasonology of Civilizations

from numpy import *
import math

Moses = 0
Liberal = 1
Lenin = 2
# define three main types of strategy

STable = zeros([3,3])
#ture table between strategies. the first one is the one who acts
# 1 is Cooperation, 0 is non-cooperation

HP = zeros([3,300])
HP[:,0] = [0.5,0.5,0.5]

def flat(n):
    result = 1 - math.exp(-n)
    return result
# sigmoid function

def antiflat(n):
    if n < 1:
        result = - math.log(1 - n)
    else:
        result = 10000
    return result
# antisigmoid function

def Gam(T1,T2):
    if T1 == 0 and T2 == 0:
        dHP = -0.10
    elif T1 == 1 and T2 == 0:
        dHP = -0.25
    elif T1 == 0 and T2 == 1:
        dHP = 0.20
    elif T1 == 1 and T2 == 1:
        dHP = 0.08
    return dHP
    # benifit rules of game

def cowork(HP1,HP2,Stype1,Stype2):

    ddHP = antiflat(HP1)*HP2*Gam(STable[Stype1,Stype2],STable[Stype2,Stype1])
#    print(ddHP)
    return ddHP
    # HP changes


STable[Liberal,:] = 1
# a Liberal loves everyone, always cooperative

STable[Lenin,:] = 0
# a Leninism hates everyone, always betray

STable[Moses,:] = 1
# Moses is cooperative in the beginning, but he can remember 

for i in range(300):
    if i < 299:
        for j in range(3):
            tHP = HP[j,i]
            for k in range(3):            
                tHP = flat(antiflat(tHP)+cowork(HP[j,i],HP[k,i],j,k)) 
                if k == Moses:
                    STable[Moses,j] = STable[j,Moses]
                    # Moses never forget
            HP[j,i+1] = tHP      


import matplotlib.pyplot as plt

plt.plot(transpose(HP[0,:]),color='green',label='Moses')
plt.plot(transpose(HP[1,:]),color='blue',label='Liberal')
plt.plot(transpose(HP[2,:]),color='red',label='Lenin')
plt.title('Seasonology of Civilizations')
plt.xlabel('time')
plt.ylabel('strength of civilizations')

plt.legend(loc='upper right')
plt.show()






