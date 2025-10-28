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

print(isAnimal)
while count < AmountOfNPCS:
    print("\nNPC", count+1)
    
    randChar = random.choice(Characteristics)

    print("Characteristic: ", randChar)

    age = random.randint(1,101)

    print("Age: ", age)


    while 1:
        floatation = random.random()*10
        if floatation > 0 and floatation < 11:
            break

    if randChar == "Anger Issues":
        print("Anger Issue trigger(tollerance, higher equal worse): ",round(floatation, 1))

    while 1:
        floatation = random.random()*10
        if floatation > 2 and floatation < 7:
            break
    
    print("The Height(feet): ", round(floatation, 1))

    isAnimal = random.randint(0,2)
    print("Is an animal: ", bool(isAnimal))

    count += 1


