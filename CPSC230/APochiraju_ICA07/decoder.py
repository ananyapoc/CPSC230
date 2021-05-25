'''User input = “aaaabbbbbcccd”
Dictionary = {“a”:4,”b”:5,”c”:3,”d”:1}
You could store the dictionary in file like this:
a,4 b,5 c,3 d,1
So that when you read it back in to create the dictionary, you can use the letters as keys and the numbers as values again.'''

userInput = input("Please give me a string ")
userDict = {}
for i in userInput:
    if i in userDict:
        userDict[i]+=1
    else:
        userDict[i]=1
print(userDict)

def dict2file(dict, myfile):
    xFile = open(myfile, "w")
    for i,j in dict.items():
        print(i,",",j,sep="",file=xFile)
    xFile.close()

dict2file(userDict,"hello.txt")

def file2dict(myfile):
    xFile = open(myfile,"r")
    dict={}
    for i in xFile:
        line=i.split(",")
        key=line[0]
        value=int(line[1])
        dict[key]=value
    xFile.close()
    print(dict)

file2dict("hello.txt")
