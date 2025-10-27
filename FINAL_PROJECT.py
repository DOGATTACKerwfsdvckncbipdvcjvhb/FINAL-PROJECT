import math
import time
import random

Characteristics = ["THE RIZZLER","Kindness","greedy","The SIGMA","Anger Issues","STUPID","DEPRESSION","CHAD","GREAT CHAD","SUPER guy","Happy","Joyfull","SIXSEVENnator","none"]
AmountOfNPCS = 0
while 1:
    AmountOfNPCS = int(input("Input amount of npcs: "))
    if AmountOfNPCS > 0 and AmountOfNPCS < 101:
        break


count = 0
while count < AmountOfNPCS:
    print("\nNPC", count+1)
    print("Characteristic: ", random.choice(Characteristics))
    print("Age: ", random.randint())
    count +=1


