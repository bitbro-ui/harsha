# make a list of 6 animals
# choose a random animal and store it in a variable called computer
# make an empty list called user and extend the answer from the computer
import time
import random
animals=["lion","goat","donkey","snake","rat","tiger",'cow','horse','gorilla']
computer=random.choice(animals)
y=list(computer)
user=[]
user.extend(y)
#print(user)
#print(computer)
#print(y)

for i in range(len(user)):
   y[i]='_'
#print(y)
print('   '.join(y))
while True:
   question=input('Type a letter on the keyboard to guess the animal\n')
   for j in range(len(user)):
      if user[j]==question:
         y[j]=question
   print('   '.join(y))
                                 


























