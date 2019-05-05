
# coding: utf-8

# In[19]:

import numpy as np;
t = int(input())
while t > 0:
    N = int(input())   # take single Integer input
    arr_v=input() # takes the whole line of n numbers
    arr_p=input() # takes the whole line of n numbers
    V = list(map(int,arr_v.split(' ')))
    P = list(map(int,arr_p.split(' ')))
    V.sort(reverse=True)
    P.sort(reverse=True)
    i=0
    win=0
    while i < N:
        if P[i] <= V[i]:
            win=1
        i=i+1
    if win==1 :
        print("LOSE")
    else :
        print("WIN")
            
    t=t-1


# In[14]:

P[0]


# In[ ]:



