import random

''' 
1 for snake
-1 for water
0 for gun
'''

try:
    computer = random.choice([1 , -1 , 0])
    #yourstr = input("Enter your choice: ")
    yourstr = input("Enter your choice : ").lower() #to ignore case sensitive
    yourdict = {"s": 1 , "w": -1 , "g": 0}# , "S":1 , "W": -1 , "G": 0} another way to solve this
    reversedict = { 1 : "Snake", -1 : "Water", 0 : "Gun"}
    you = yourdict[yourstr]
    
    print(f"You chose {reversedict[you]}\n computer chose {reversedict[computer]} ")
    
    if (computer == you):
        print("Its a draw")
        
    else:
        if (computer == -1 and you == 1):
            print("You win!")
        
        elif (computer == -1 and you == 0):
            print("You lose!")
            
        elif (computer == 1 and you ==-1):
            print("You lose!")
            
        elif (computer == 1 and you == 0):
            print("You win!")
            
        elif (computer == 0 and you == -1):
            print("You win!")
            
        elif (computer == 0 and you == 1):
            print("You lose!")
            
        else:
            print("Something went wrong")
     
except:
    print("Please enter valid input (s , w or g)")
