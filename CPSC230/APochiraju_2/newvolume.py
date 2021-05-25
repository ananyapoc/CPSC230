#this is to calculate the volume of a cylinder
import math
#asking the user for inputs
r=int(input("give me a length for the radius of the cylinder"))
#stating conditions for radius
if(r==0):
    print("please do not give zero")
elif(r!=0):
    h=int(input("give me a length for the height of the cylinder"))
#stating conditions for height
if(h==0):
    print("please do not give zero")
elif(h!=0):
    print((r*r)*h*math.pi) #calculating the volume using pi
