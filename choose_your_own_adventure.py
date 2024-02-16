#choose your own adventure game (project 4)
print("Welcome to the adventure game....")
name=input("Type your name: ")
print(f"Now,{name} choose your own adventure path.Choose wisely")
q1=input("You are in the middle of a jungle and you are alone.Do you want to stay here for rest of your life or you want to run?If you want to stay here type stay else type run:(stay/run )").strip().lower()
if q1=="stay":
    q2=input("Okay,You choose to stay here.So, you need to build a house in the jungle and for that you need wood.Do you want to walk around to find wood?Type yes/no").lower()
    if q2=="yes":
        q3=input("you were walking around to find wood but you came across in front of a Beer.What do you want to do now?(Lay Down or Run): ").lower()
        if q3=="lay down":
            
            print("You laid down and the beer killed you and you lost the game")
        elif q3=="run":
            print("you ran away and found a way out of the jungle ")
        else:
            print("You have failed to make any decision and the beer killed you")
        
    elif q2=="no":
        print("Without a house in the jungle, you can't survive here. Tiger will eat you alive. So, you failed")
    else:
        print("You have failed to make any decision and you died ..")
      
elif q1=="run":
    q=input("You have chosen to run away from jungle.After running for a while you found a river. Do you want to cross it?(yes/no): ").lower()
    if q=="yes":
        q=input("How do you want to cross the river?(Swim/Boat): ").lower()
        if q=="swim":
            print("you tried to cross the river by swimming but there was a crocodile and it killed you")
        elif q=="boat":
            q=input("You have chosen to cross the river by boat.So, you need wood to make boat and for that you need to go back to the jungle again. What do you want to do now?(go back/swim): ").lower()
            if q=="go back":
                print("There was a lion in the jungle and it killed you") 
            elif q=="swim":
                print("There was a crocodile in the river and while crossing the river by swimming it killed you")
            else:
                print("There was a snake at the bank of the river and it bit you and you died there..")
        
        
        
    
    elif q=="no":
        q=input("You chose not to cross the river.So, what do you want to do now?(go back/stay): ").lower()
        if q=="go back":
            print("There was a lion in the jungle and it killed you")
        elif q=="stay":
            print("There was a snake at the bank of the river and it bit you and you died there..")
        else:
            print("There was a snake at the bank of the river and it bit you and you died there..")
            
    else:
        print("You have failed to make any decision and you died at the bank of the river")

else:
    print("You have failed to make any decision and you died ..") 
print("Game over . That was an endless game haha haha.....There was no chance for surviving....")
