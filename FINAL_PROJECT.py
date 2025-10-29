import math #imports the math library
import time #imports the time library
import random #imports the random library

#the traits of the character
Characteristics = ["THE RIZZLER","Kindness","greedy","The SIGMA","Anger Issues","STUPID","DEPRESSION","CHAD","GREAT CHAD","SUPER guy","Happy","Joyfull","SIXSEVENnator","none","VERY CHARMING","VERY SPECIAL"]

#Variable declaration
AmountOfNPCS = 0

#This function will generate an npc that is randomized
def GenerateNPC():
     #gets a random trait from the list called characteristics
    randChar = random.choice(Characteristics)
    

    #prints the random trait from the variable randChar
    print("Characteristic: ", randChar)
    

    #gets a random number for age
    age = random.randint(1,101)
    

    #prints the age
    print("Age: ", age)
    

   
    #gets a random float, unlike 
    intensity = random.uniform(1,10)

    #Checks if the randchar variable is not "none" from the list
    if randChar != "none":
        #prints an intensity of that trait in the character
        print("Intensity of trait(10 is intense): ",round(intensity, 1))
    
    
    
    height = random.uniform(2,7)

    #prints the height of the character
    print(f"The height is   {round(height, 1)}   ft", )

    #makes a random integer from 0 to 10
    isAnimal = random.randint(0,11)

    #if statement to change the probability from 50/50 to 30/70
    if isAnimal < 4:
        #sets is animal to true
        isAnimal = 1
        
    else:
        #sets is animal to false
        isAnimal = 0
        

    #prints if the character will be an animal, it also typecasts the variable to a boolean
    print("Is an animal: ", bool(isAnimal))
    

    #new line
    print()

#Enter a while loop
while 1:
    #get the amount of npcs the user wants
    AmountOfNPCS = int(input("Input amount of npcs(1 to 30): "))
    #if statement to make sure user does not enter negative or to high numbers
    if AmountOfNPCS > 0 and AmountOfNPCS < 31:
        #breaks condition if true
        break
    
    print("INVALID INPUT")

#Variable declaration
count = 0



#Enters the primary while loop to print npcs
while count < AmountOfNPCS:
    #prints the npc the loop is on
    print("\nNPC", count+1)
    
    GenerateNPC()
    
    #increment count by 1
    count += 1
    
    
    #adds a slight delay to the loop
    time.sleep(0.2)
  


