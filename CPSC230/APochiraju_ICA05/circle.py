import math
def radius():
    x=float(input("Please give a float radius value "))
    return x

def diameter(x):
    d=x*2
    return d

def circumference(x):
    c=math.pi*2*x
    return c

def area(x):
    a = math.pi*x**2
    return a

def information():
    r = radius()
    print("The diameter is",diameter(r))
    print("The circumference is",circumference(r))
    print("The area is",area(r))
information()
