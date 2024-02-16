#Number Guessing Game
name=input("Whats your name? ").title()
print(f"Hello {name},Welcome to the number guessing game.")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
     print("Please type a number next time. Bye")
     quit()       
#importing random number generator
import random
random_number = random.randrange(top_of_range)
#to keep track of the guesses .That means how many times the while loop has executed
guesses=0

    

#checking if the guessed number is correct or not by while loop
#if the use guess the correct number we will quit the while loop    
#if not we will continue asking to guess by while loop
while True:
    #i also want to keep track of how many times user guessed the number before getting it correct
    guesses+=1
    
    #asking user to guess the random number

    user_guess=input("Guess a number: ")
#checking: user guessed a number or not
# #if the typed a number then we need to convert it to integer
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time")
        continue    
    if user_guess==random_number:
        print("You got it correct!")
        break
    else:
        # now we want to tell the user if they were above the random number or below the random number
        if user_guess>random_number:
            print("You were above the number")
        else:
            print("you were below the number")    
        
             

print(f"You got it correct in {guesses} guesses")
    
        
    
     