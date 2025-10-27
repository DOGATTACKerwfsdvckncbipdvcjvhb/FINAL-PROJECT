import math
import time
import random

Characteristics = ["THE RIZZLER","Kindness","greedy","The SIGMA","Anger Issues","STUPID","DEPRESSION","CHAD","GREAT CHAD","SUPER guy","Happy","Joyfull","I DONT KNOW","SYSTEM ERROR"]
AmountOfNPCS = 0
while 1:
    AmountOfNPCS = int(input("Input amount of npcs: "))
    if AmountOfNPCS > 0 and AmountOfNPCS < 101:
        break


count = 0
while count < AmountOfNPCS:
    print("NPC", count+1)
    print("Characteristic: ", random.choice(Characteristics))
    print("\n\n\n")
    count +=1


