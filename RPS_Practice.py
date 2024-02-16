import random
option=["rock","paper","scissor"]
user_point=0
computer_point=0
pick=input("Rock/Paper/Scissors/Q(to quit game): ").lower().strip()
if pick == "q":
    quit()
else:
        
    while True:
        pick=input("Rock/Paper/Scissors/Q(to quit game): ").lower().strip()
        if pick=="q": 
            break
        if pick not in option:
            continue
    
        random_number=random.randint(0,2)
        computer_pick=option[random_number]
        if pick=="rock" and computer_pick=="paper":
            print("You Won!")
            user_point+=1
        elif pick=="paper" and computer_pick=="scissor":
            print("You Won!")
            user_point+=1   
        elif pick=="scissor" and computer_pick=="rock":
            print("You Won!")
            user_point+=1 
        
        else:
            print("Computer won!")    
            computer_point+=1
        

print("You won",user_point,"times.")
print("Computer won",computer_point,"times.") 

if user_point>computer_point:
    print("Congo,You are the champion") 
elif user_point==0 and computer_point==0:
    print("You didn't even try")     
elif user_point==computer_point:
    print("Match Draw")

else:
    print("Sorrrrrrrry, You have lost the game. Try Again Next Time")
        
        
    