# #!/usr/bin/python3

import random
import time

print("Welcome to the Capitals Quiz Game!")
print("You have 1 mistake allowed at first, then 3, and finally 10 seconds to answer.")
print("Let's start!")
print("")

countries={
    "Japan":"Tokyo",
    "Armenia":"Yerevan",
    "Spain":"Madrid",
    "USA":"Washington",
    "Russia":"Moscow",
    "German":"Berlin",
    "South Korea":"Seoul",
}

ml = list(countries.items())
random.shuffle(ml)

# All countries,but 1 mistake
for el in ml:
    print('WHat is the capital of %s' %el[0])
    answer = input('Enter your answer: ')
    if answer.lower() == el[1].lower():
        print('correct')
    else:
        print('boom 1')
        break

# All countries,but 3 mistake
count = 3
for el in ml:
    print('What is the capital of %s' % el[0])
    if (count == 0):
        print('Boom 2')
        break
    answer = input('Enter your answer: ')
    if answer.lower() == el[1].lower():
        print('Correct!')
    else:
        count -= 1
        print('Incorrect.You have %d attend' %count)

 # 10 seconds to think
print("You have 10 second to answer!") 
print('What is the capital of %s' % el[0])

 #Timer
t = 10
while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'. format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
    
answer = input('Enter your answer: ')
if answer.lower() == el[1].lower():
    print('Correct! You win !')
    
else:
    print("Game over. You lost !")

