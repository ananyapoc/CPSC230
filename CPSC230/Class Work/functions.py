
#1)define function
#2)use that function

def adder():    #defining function with no parameters
    print(3+1)

adder()    #calls function and prints 4

--------------------------------------------------------------------------------

def adder():
    result = 3+1
    return result

adder()    #result is being returned but it's not stored anywhere

 --------------------------------------------------------------------------------

def adder():
    result = 3+1
    return result

l = adder()    #now result is being stored in l
print(l)       #prints 4

# OR YOU CAN DO THIS INSTEAD:
print(adder())

--------------------------------------------------------------------------------

#question on the exam: what does the function do?
#this function^^ adds 3 to 1

--------------------------------------------------------------------------------

def adder(x,y):          #now this function has two parameters
    result = x+y
    return result

#you need to add parameters when calling the function now or you'll get an error
print(adder(6,7))     #prints 13 bc it adds x and y

#YOU CAN'T CALL THE FUNCTION BEFORE YOU DEFINE IT.

--------------------------------------------------------------------------------

def func1(a):         #takes one parameter
    return a[0]       #returns the first element of a collection

print(func1("hello"))    #prints 'h'
print(func1([1,"1"]))    #prints 1

--------------------------------------------------------------------------------

#write a function isEvens that returns True if the single parameter is even
#otherwise return False

def isEvens(x):
    if x%2 == 0:          #checks if even or not
        return True
    else:
        return False

print(isEvens(6))       #prints True
print(isEvens(55))       #prints False

--------------------------------------------------------------------------------

a = [1,2,3]
print(len(a))

def length(lst):     #defining a function that does the same thing as the len() function
    count = 0
    for i in lst:
        count+=1
    print(count)
    return count      #return has to be the last line bc it breaks the defining of the function

length(a)     #prints 3 bc the print statement is in the definition
