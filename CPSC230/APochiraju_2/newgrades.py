#asking user for test scores to find an average
a=int(input("please give me a test score out of 100"))
b=int(input("a second test score out of 100"))
c=int(input("and a third test score"))
print((a+b+c)/3) #will calculate the avg of the 3 scores
m=((a+b+c)/3) #m for mean (average)
#stating the various conditions
if(m>=90):
    print("You get an A!")
elif(80<=m<90):
    print("You get a B")
elif(70<=m<80):
    print("You get a C")
elif(60<=m<70):
    print("You get a D")
elif(m<60):
    print("You get an F")
