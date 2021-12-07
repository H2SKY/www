#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print('Hello, what is your name?')

name = str(input())
answer = random.randint(1, 100)

print('Well, ' + name + ', I am thinking of a number from 1 to 100.You have only 10 guesses')

guessesTaken = 0
guessedCorrectAnswer = False

while guessesTaken < 10:
    print('Take a guess.')

    guess = input()
    guessesTaken = guessesTaken + 1

    try:
        if int(guess) == answer:
            guessedCorrectAnswer = True
            print('Good job, ' + name +
                  '! You guessed my number in ' + str(guessesTaken) +
                  (' guess!' if guessesTaken == 1 else ' guesses!'))
            break
        elif int(guess) < answer:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')
    except ValueError:
        guessesTaken = guessesTaken - 1
        print('You must enter a number.')

if not guessedCorrectAnswer:
    print('Next time. The number I was thinking of was ' + str(answer) + '.')


# In[ ]:




