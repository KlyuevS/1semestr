#!/usr/bin/env python
# coding: utf-8

# In[12]:


myString=input()
newString=(myString[1:len(myString)-1])
print(myString[len(myString)-1]+newString+myString[0])


# In[ ]:


n=int(input())
factorial=1
while n>1:
    factorial=factorial*n
    n=n-1

print(factorial)


# In[10]:


import random
human=input("Your choice:rock, paper or scissors")
tools=["rock","paper","scissors"]
computertools=random.choice(tools)
if human == computertools:
    print(f"Both pick {human}. nobody win")
elif human == "rock":
    if computertools == "scissors":
        print("rock stronger than scissors, u win")
    else:
        print("paper stronger than rock. u lose((")
elif human == "paper":
    if computertools == "rock":
        print("paper stronger than rock, u win")
    else:
        print("scissors stronger than rock, u lose =(")
elif human == "scissors":
    if computertools == "paper":
        print("scissors stronger than paper, u win!)")
    else:
        print("rock stronger than scissors, u lose=(")


# In[ ]:





# In[ ]:




