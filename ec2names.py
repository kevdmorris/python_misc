#EC2 Random Name Generator
import random

vowels = ["A","E","I","O","U"]
cons = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]

def builtWord():
    randomNumber = random.randint(8, 12)
    name=""
    for i in range(randomNumber):
        randomVowel= random.choice(vowles)
        randomCons = randon.choice(cons)
        name= name + randomVowel + randomCons
    return name

print(builtWord()

#print(cons)



#name generator

#name = random.choice

#print(name)

