print("Welcome to my Game")
game = input('Do you want to play the game? ').lower().strip()
if game=="yes":
    print("Let's Play")
if game == "no":
    print("Okay, Bye. You Dumb Ass")
    quit()
print("Before starting the game we need to ask you some questions") 
#personal Questions
q1=input("What is your name? ").strip().title()   
print(q1)
q2=input("Where do you live in? ").strip().title()
print(q2)
q3= input("What do you do for living? ").strip().title()
print(q3)
print(f"Hello,{q1}.Let's play the game now..........")