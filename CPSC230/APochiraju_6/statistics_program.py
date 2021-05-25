#this code is to find the mean, standard deviation, and variation of a list of numbers
import math
finallist = []
while(True):
    userInput=int(input("Please give me a positive number "))
    if(type(userInput)==int and userInput>=0):
        finallist.append(userInput)
        continue
    else:
        finallist.append(userInput)
        break
print(sorted(finallist))

#finding mean
x=0
for v in finallist:
    x+=v
mean = x/len(finallist)
print("The mean is", mean)

#finding variance
variance = 0
for i in finallist:
    variance +=(float(i)-mean)**2

#finding standard deviation
stndeviation = 0
for i in finallist:
    stndeviation = math.sqrt(variance)
print("The standard deviation is", stndeviation)
