# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:43:16 2019

@author: EYENIKE
"""

from random import randint

print(
"""Instruction
This game requires you to try to guess the random number generated by the computer. If you guess the right number then you win the game.\n
""")

random_number = randint(1,100)
count = 0

while True:
    
    my_number = int(input("Please input your guessed number:"))
    
    count += 1
    
    if count <= 8:
        if my_number == random_number:
            print("\nYou guessed right, Congrat!!!\n")
            print("It took you " + str(count) + " guesses to get the answer\n")
            break                                                                                                        
        elif my_number > random_number:
            print("You guessed to high")
        elif my_number < random_number:
            print("You guessed to low")
    else:
        print("You reached the required number of guesses which is 8\n")
        print("Sorry you failed the tesT")
        break
        

print("The correct answer is " + str(random_number))
