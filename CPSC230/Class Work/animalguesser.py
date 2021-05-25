def AnimalGuesser():
    numlegs = int(input("Please give me the number of legs on the animal you are" \
    "looking at and I will tell you if it is a crab, dog, spider, or person "))
    animal = ""
    if numlegs == 2:
        animal = "person"
    if numlegs == 10:
        animal = "crab"
    if numlegs == 4:
        animal = "dog"
    if numlegs == 8:
        animal = "spider"
    return animal
print(AnimalGuesser())
