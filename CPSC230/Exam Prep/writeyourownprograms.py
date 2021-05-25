def counter(userList):
    vowels = "aeiouAEIOU"
    count = 0
    for i in userList:
        if i[0] in vowels:
            count+=1
    return count
print(counter(["apple","banana","Orange","Grape"]))

firstlist = []
a = int(input('Please give a number '))
b = int(input('Please give a second number '))
c = int(input('Please give a third number '))
firstlist.append(a)
firstlist.append(b)
firstlist.append(c)
finaltuple = tuple(firstlist)
print(finaltuple)

def separator(fullname):
    fullnamelist = fullname.split(" ")
    middlename = fullnamelist[1]
    firstname = fullnamelist[0]
    lastname = fullnamelist[2]
    middleinitial = middlename[0]
    print(lastname,",",firstname,middleinitial,".")
separator("Rao Hamza Ali")

def comparator(atuple,n):
    finallist = []
    for i in atuple:
        if len(i)>n:
            finallist.append(i)
    return finallist

print(comparator(("fun","banana","tree","dog"),3))

numbers = input("Please give me a lot of single digit numbers ")
sum = 0
for i in numbers:
    i = int(i)
    sum+=i
print(sum)

def alternator(strA,strB):
    x=0
    r=""
    if len(strA)>len(strB):
        longerword = strA
    else:
        longerword = strB
    for i in longerword:
        if len(strA)>=(x+1):
            r = r+strA[x]
        if len(strB)>=(x+1):
            r = r+strB[x]
        x+=1
    return r

print(alternator("pie","and"))
