import matplotlib.pyplot as plt
import random as r
trials=10000
x=[i for i in range(trials)]

N=S=0
y=[]
y1=[]
for i in range(1,trials+1):
    win  = r.randint(0,1) # system win amount
    choi = r.randint(0,1) # choise by player
    switch = r.randint(0,1)

    if switch and choi==win:
        S+=1
    elif switch==0 and choi==win:
        N+=1
    y.append(N/i)
    y1.append(S/i)
plt.plot(x,y)
plt.plot(x,y1)
plt.show()





