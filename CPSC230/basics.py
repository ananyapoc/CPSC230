candy = {"Max":"Twix","Seth":"Almonds","Rao":"Licorice","Rao":"SPK"}
#candy["new key"] = value
candy["Max"] = "Mounds"
#dictionaryname[key]
for i in candy.items():
    print(i)
for i in candy.keys():
    print(i)
for i in candy.values():
    print(i)

d = {1:"hello",2:"world"}
d[3]="universe"
d["yay"]=50
for i in d.values():
    print(i)
for i in d.items():
    print(i)

try:
    a = int(input("give a "))
    b = int(input("give b "))
    print(a/b)
except ZeroDivisionError:
    b = int(input("another b please"))
    print(a/b)
print("hello world")

myfile = open("hello.txt","r")
myfilecontents = myfile.readlines()
myfile.close()
#for lines in myfile:
#    print(lines)
print(myfilecontents)

myfile = open("goodbye.txt","w")
print("goodbye world",file=myfile)
myfile.close()

inFile = open("goodbye.txt","r")
lst = inFile.readlines()
print(lst)
inFile.close()

evensFile = open("evens.txt","w")
oddsFile = open("odds.txt","w")
for i in range(0,101):
    if i%2 == 0:
        print(i,file=evensFile)
    else:
        print(i,file=oddsFile)

evensFile = open("evens.txt","r")
oddsFile = open("odds.txt","r")
#method with a for loop
evensList = []
for i in evensFile:
    evensList.append(int(i))
print(sum(evensList)/len(evensList))
#method with readlines function
oddsList = oddsFile.readlines()
oddsList2 = []
for i in oddsList:
    oddsList2.append(int(i))
print(sum(oddsList2)/len(oddsList2))
evensFile.close()
oddsFile.close()
