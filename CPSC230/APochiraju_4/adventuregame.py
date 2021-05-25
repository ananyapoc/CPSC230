import random

# variable creation & setting loop control variable
room = 1
# generating a random number
death_die = random.randint(1,100)


while room != 0:
    if room == 1:
        print('You are in a small room. There is a "closet" and a doorway to the "hall".' )
        print()
        choice = input('Which room would you like to choose? ')
        if choice == 'closet':
            if death_die > 88:
                print("You were mauled by a vampire! RIP.")
                room = 0
            else:
                room = 2
                death_die = random.randint(1,100)
        elif choice == 'hall':
            room = 3
        else:
            print(choice, " wasn't one of the options. Try again." )
# section for choosing 'closet'
    elif room == 2:
        print('You\'re in a barren closet. There\'s nothing to do here except go "back".' )
        print()
        choice = input('Write "back" to go back. ')
        if choice == "back":
            room = 1
        else:
            print(choice, " wasn't one of the options. Try again." )
#section for choosing 'hall'
    elif room == 3:
        print('You are in the hall. You can either go to another "room" of the house, or go to the "yard".' )
        print()
        choice = input('Where would you like to go? ')
        if choice == 'room':
                room = 4
        elif choice == 'yard':
                room = 5
        else:
            print(choice, "wasn't one of the options. Try again." )
#section for choosing 'room'

    elif room == 4:
        print('You are in a big spooky room. You see a set of "stairs" infront of you. There is also an "escalator".' )
        print()
        choice = input ('Choose your poison, if you dare. ')
        if choice == 'stairs':
            death_die = random.randint(1,50)
            if death_die < 50:
                print("The creepy Chucky doll at the bottom of the stairs came alive and ate your head! You are dead. Goodbye. ")
                room = 0
        elif choice == 'escalator':
                print("Oops! Looked like you ran into the scary clown. He suffocated you. Bye. ")
                room = 0
        else:
            print(choice, "wasn't one of the options. You scared? Try again.")
#section for choosing 'yard'
    elif room == 5:
        print('Welcome to the yard. Notice all the rotting skulls around you. Just kidding! There is no yard. Go back. ')
        print()
        choice = input('Write "back" to go back. ')
        if choice == "back":
            room = 6
        else:
            print(choice, " wasn't one of the options. Try again." )
#section for coming back from 'yard'
    elif room == 6:
        print('Well, looks like you are back in the house. Want to keep going?' )
        print()
        choice = input('What room do you want to explore next? Room 2 or Room 3? ')
        if choice == 'Room 2':
            room = 4
        elif choice == 'Room 3':
            room = 7
        else:
            print(choice, "wasn't one of the options. Try again." )
#section for choosing 'Room 3'
    elif room == 7:
        print('I am very surprised you have got this far. Good job! You have found the treasure! Now leave.' )
        break
