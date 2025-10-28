import math
import time
import random

Characteristics = ["THE RIZZLER","Kindness","greedy","The SIGMA","Anger Issues","STUPID","DEPRESSION","CHAD","GREAT CHAD","SUPER guy","Happy","Joyfull","SIXSEVENnator","none"]
AmountOfNPCS = 0
while 1:
    AmountOfNPCS = int(input("Input amount of npcs: "))
    if AmountOfNPCS > 0 and AmountOfNPCS < 101:
        break

age = 0

count = 0
isAnimal = random.randint(0,2)
print(isAnimal)
while count < AmountOfNPCS:
    print("\nNPC", count+1)
    randChar = random.choice(Characteristics)
    print("Characteristic: ", randChar)
    age = random.randint(1,101)
    print("Age: ", )
    floatation = random.random(1.0, 10.0)
    if randChar == "Anger Issues":
        print("Anger Issue trigger: ",floatation)

    floatation = random.random(2.0, 6.7)
    
    print("The Height: ", floatation)

    count += 1


