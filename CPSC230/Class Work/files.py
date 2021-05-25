evensFile = open("evens.txt","r")
oddsFile = open("odds.txt","r")
evensList = []
for i in evensFile:
    evensList.append(int(i))
print(sum(evensList)/len(evensList))

def averageCalculator(fileName):
    myfile = open(fileName,"r")
    mylist = []
    for i in myfile:
        mylist.append(int(i))
    print("your average is",sum(mylist)/len(mylist))
    myfile.close()

averageCalculator("evens.txt")
