import random
from itertools import permutations
combos=[]
score=0
guesses=0
response1="yes"
response="yes"
mytuple = ("broomstick", "candy", "corpse", "demon", "disguise")

while(response1=="yes"):
    b=random.choice(mytuple)
    for i in permutations(b):
        v=combos.append(i)
    random=random.choice(combos)
    random=''.join(random)

    while(guesses<3):
        print(random)
        answer=input("Try to guess what word this came from ")
        if(answer!=b and guesses<3):
            print("Please try again.")
        elif(answer!=b and guesses >=3):
            response=input("Sorry, you got it wrong. Want to try another word? ")
            break
        elif(answer==b and guesses<3):
            score+=1
            print("Correct! Your score is", score)
            response1=input("Would you like to try a different word? ")
            break

    response=response.lower()
    if(response=="yes"):
        continue
    else:
        print("goodbye")
        break
