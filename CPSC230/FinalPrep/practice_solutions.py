# 1)

userInput = input("Enter a string:")
userInput = userInput.lower()
updateString = ""
for i in userInput:
    if i in 'aeiou':
        updateString+=i.upper()
    else:
        updateString+=i
print(updateString)


#2)

write_file = open("uppercase.txt", "w")
while True:
    filename = input("Enter the name of a file to read: ")
    try: # try to open a file given a name
        f = open(filename, "r")
        for line in f:
            write_file.write(line.upper())
        f.close()
        break # program reaches here if file is read successfully so end loop
    except FileNotFoundError:
        print("That file does not exist. Try again.")
write_file.close()

#3)

def check_alternating(s):
    s1 = s[::2] # get alternative strings
    s2 = s[1::2]

    # if each substring of s is uppercase and lowercase respectively, then it's true
    if (s1.isupper() and s2.islower()) or (s2.isupper() and s1.islower()):
        return True
    else:
        return False

print(check_alternating("aBcD"))
print(check_alternating("abCd"))


#4)

while True:
    u_score = input("Enter your score: ")
    try:
        u_score = float(u_score)
        break # if the program has reached this point, casting was successful
        # and the while loop should be broken so the program can end.
    except ValueError:
        print("Not a valid score, enter again.")
if(u_score >= 90):
    print("A")
elif(u_score >= 80):
    print("B")
elif(u_score >= 70):
    print("C")
elif(u_score >=60):
    print("D")
else:
    print("F")

#5)

try:
    my_function()
except ErrorA:
    print("Your function caused ErrorA")
except ErrorB:
    print("Your function caused ErrorB")


#6)

userInput = input("enter five words, comma separated:")
inputList = userInput.split(",")
outFile = open("hello.txt","w")
for i in inputList:
    print(i,file=outFile)
outFile.close()
# now read file
inFile = open("hello.txt","r")
for i in inFile:
    print(len(i.strip())) # important to string so \n is not counted
inFile.close()


#7)

a = [1,2,3]
b = [4,5]

a.extend(b)
print("sum is ",sum(a))
print("average is ",sum(a)*1.0/len(a))
if len(a)%2 == 0: # if list is of even length
    midInd = len(a)//2
    midInd2 = midInd-1
    print("median is ",(a[midInd]+a[midInd2])/2) # then median is average of two middle values
else:
    print("median is",a[len(a)//2]) # otherwise, find the middle index


#8)
alist = [1,2,3,4,5]
while True:
    n = int(input("enter number to remove"))
    try: # try to remove, if it doesn't exist, then ValueError is raised
        alist.remove(n)
        break
    except ValueError:
        print("Try again!")
