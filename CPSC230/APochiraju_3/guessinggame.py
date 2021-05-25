#this is the guessing game to solve what the number is
import random
n=random.randint(0,100)
while(True): #establishing while loop for the game
    g=int(input("please guess a number between 0 and 100: "))
    while(g!=n):
        if(g<n):
            print("your guess is too low. try again!")
        elif(g>n):
            print("your guess is too high. try again!")

    if(g==n):
        print("you have won!")
        r=input("would you like to play again? ") #bonus section

        if(r=="YES"):
            continue  #brings to the top of the loop
            n=random.randint(0,100)
        else:
            break  #exit strategy to end the whole program
    continue #restarts the game
