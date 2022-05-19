"""
Guess the number game
"""
import random

value = int(input("Please enter a number from 0 - 100: "))

number = random.randint(0,100)

print(number)

if number == 13:

    print("Your are correct!")

if number > 13:

    print("Your are too high.")

if number < 13:

    print("You are too low.")

#print (number, " < 13: Your number is too low")