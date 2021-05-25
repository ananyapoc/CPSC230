import random
listOfWords = ['cat','castle','pizza','balloon']

def grabWord(c):
    return random.choice(c)

def cloudLike():
    print("That cloud looks like a",grabWord(listOfWords))


def multiplexer(x):
    y = 1
    for i in range(1,x+1):
        y*=i
    return y

def calculator(z):
    lst = []
    for i in range(1,z+1):
        lst.append(multiplexer(i))
    return lst

tupleA = [[1,2,3],[4,5,6]]
totalCounter = 0
for i in tupleA:
    for e in i:
        totalCounter+=1
print(totalCounter)

def func(param1,param2):
    param2.insert(1,3)
    param2.extend(param1)
    return param2.pop(0)

one = (1,2)
two = ["1","3"]

result = func(one, two)
print(result)
print(one)
print(two)
