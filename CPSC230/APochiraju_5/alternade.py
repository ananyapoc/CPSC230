#asking user for words to either create an alternade or two words from an alternade
x=0
r=""
i=0
choice=input("Would you like to construct or deconstruct? ")
if choice == "construct":
    a=input("Please give me a word ")
    b=input("Please give me another word ")
    while a.isalpha() and b.isalpha()!= True:
        a=input("Letters only. No numbers")
        b=input("Letters only. No numbers or other characters")
else:
    c=input("Please give me one word ")
    while c.isalpha() !=True:
        c=input("Letters only. No numbers or other characters")
#section if user wants to construct
if choice == "construct":
    if len(a)>len(b):
        longerword=a
    else:
        longerword=b
    for i in longerword:
        if(len(a)>=(x+1)):
            r=r+a[x]
        if(len(b)>=(x+1)):
            r=r+b[x]
        x+=1
    print("Your word is" , r)
#section if user wants to deconstruct
elif choice == "deconstruct":
    listA=[];
    listB=[];
    len(c)
    wordlength=len(c)
    if len(c) % 2:
        wordlength+=1
        c+=" "
    while i < len(c):
        c[i]
        c[i+1]
        listA.append(c[i])
        listB.append(c[i+1])
        i+=2
        strA = ''.join(listA)
        strB = ''.join(listB)
    print(strA)
    print(strB)
