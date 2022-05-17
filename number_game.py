"""
Guess the number game
"""
import random

value = str(input("Please enter a number from 0 - 100: "))

number = random.randint(0,100)

if number > 13:

    print(" Your are too high")

#print (number, " < 13: Your number is too low")