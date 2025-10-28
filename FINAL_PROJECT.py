import math #imports the math library
import time #imports the time library
import random #imports the random library

#the traits of the character
Characteristics = ["THE RIZZLER","Kindness","greedy","The SIGMA","Anger Issues","STUPID","DEPRESSION","CHAD","GREAT CHAD","SUPER guy","Happy","Joyfull","SIXSEVENnator","none","VERY CHARMING","VERY SPECIAL"]

AmountOfNPCS = 0
#Variable declaration

#Enter a while loop
while 1:
    #get the amount of npcs the user wants
    AmountOfNPCS = int(input("Input amount of npcs: "))
    #if statement to make sure user does not enter negative or to high numbers
    if AmountOfNPCS > 0 and AmountOfNPCS < 31:
        break
        #breaks condition if true

age = 0; count = 0
#Variable declaration


#Enters the primary while loop to print npcs
while count < AmountOfNPCS:
    print("\nNPC", count+1)
    #prints the npc the loop is on
    
    randChar = random.choice(Characteristics)
    #gets a random trait

    print("Characteristic: ", randChar)
    #prints the random trait from earlier on line 29

    age = random.randint(1,101)
    #gets a random number for age

    print("Age: ", age)
    #prints the age

    #Infinite while loop to make sure the float is not to small
    while 1:
        #gets a random float
        floatation = random.random()*10
        #checks if the float is between the boundries
        if floatation > 0 and floatation < 11:
            break
            #breaks if true

    #Checks if the randchar variable is not "none" from the list
    if randChar != "none":
        #prints an intensity of that trait in the character
        print("Intensity of trait(10 is intense): ",round(floatation, 1))
    
    #same thing as line 42
    while 1:
        floatation = random.random()*10
        if floatation > 2 and floatation < 7:
            break

    #prints the height of the character
    print(f"The height of them is   {round(floatation, 1)}   feet/foot", )

    #makes a random integer from 0 to 10
    isAnimal = random.randint(0,11)

    #if statement to change the probability from 50/50 to 30/70
    if isAnimal < 4:
        isAnimal = 1
        #sets is animal to true
    else:
        isAnimal = 0
        #sets is animal to false

    print("Is an animal: ", bool(isAnimal))
    #prints if the character will be an animal, it also typecasts the variable to a boolean

    print()
    #new line

    count += 1
    #increment count by 1
    
    time.sleep(0.2)
    #adds a slight delay to the loop


