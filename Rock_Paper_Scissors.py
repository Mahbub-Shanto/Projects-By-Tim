#Rock,paper,scissors game
#first we need to generate random numbers
#it's a good practice to import at the beginning of the  code
import random
#initializing the score of user and computer , both of them are integers
user_win=0
computer_win=0
options=["rock","paper","scissors"]
# options are in a list 
#lists serial begins from 0

#now we need to ask the user  if they want to play or not. 
ask=input("Do you want to play?(Yes/No) ").lower()
if ask!= "yes":
    quit()
else:
    while True:
        
    #ask user to type rock/paper/scissor
        user_input=input("Type Rock/Paper/Scissors/Quit to stop playing: ").lower()
        if user_input=="quit": 
            break
        if user_input not in options:
            continue
        
        #generating random numbers
        random_number=random.randint(0,2)
        #rock:0,paper:1,scissor:2
        computer_pick=options[random_number]
        print(f"Computer picked {computer_pick}")
        if user_input=="rock" and computer_pick=="paper" :
            print("You won!")
            user_win+=1
        elif user_input=="paper" and computer_pick=="scissors" :
            print("You won!")
            user_win+=1 
        elif user_input=="scissors" and computer_pick=="rock" :
            print("You won!")
            user_win+=1
        else:
            print ("You Lost")
            computer_win+=1
print(f"you won {user_win} times") 
print(f"Computer won {computer_win} times")   
print("GoodBye")           