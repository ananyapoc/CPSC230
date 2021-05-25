#1)
'''userInput = str(input("Please give me a string "))
lowerInput = userInput.lower()
newstring = ""
for i in lowerInput:
    if i in "aeiou":
        newstring+=i.upper()
    else:
        newstring+=i
print(newstring)

#2)
upperFile = open("uppercase.txt","w")
while True:
    file = input("Please give me a file to read. ")
    try:
        f = open (file,"r")
        for line in f:
            upperFile.write(line.upper())
        f.close()
        break
    except FileNotFoundError:
        print("Sorry! Couldn't find that file. Please enter another one: ")
upperFile.close()

#3)
def checkalternate(str):
    s1=str[::2]
    s2=str[1::2]

    if(s1.isupper() and s2.islower()):
        return True
    elif(s2.isupper() and s1.islower()):
        return True
    else:
        return False

print(checkalternate("aBcD"))
print(checkalternate("ABcD"))

#4)
while True:
        userInput = input("Please give me a test score: ")
        try:
            testscore=float(userInput)
            break
        except ValueError:
            print("Please give a correct input.")
            continue

if testscore>=90 and testscore<=100:
    print("Congrats, you got an A!")
elif testscore>=80 and testscore<=89.9:
    print("You got a B!")
elif testscore>=70 and testscore<=79.9:
    print("You got a C")
elif testscore>=60 and testscore<=69.9:
    print("You got a D")
else:
    print("Sorry, you got an F")

#5)
try:
    myfunction()
except ErrorA:
    print("You got Error A")
except ErrorB:
    print("You got Error B")
