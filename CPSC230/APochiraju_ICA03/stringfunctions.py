#Question 1
var1="You're a wizard, Harry!"
var2="1234567890"
var3="up up down down left right left right B A"
print(var1[17:22])
print(var3.upper())
print(var1.lower())
print(var3.title())
print(var2.isnumeric())
print(var2.isdecimal())
print(var3.replace("up","left").replace("down","right").replace("left","up").replace("right","down"))
print(var3.find("below"))

#Question 2
while(True):
    p=str(input("make a strong password"))
    if(len(p)<8):
        print("Password is too short")
        continue
    else:
        p.find("?")
        if(p.find("?")==-1):
            print("Password must contain atleast 1 question mark")
            continue
        else:
            p.find("cat")
            if(p.find("cat")==-1):
                print("Password must contain cat atleast once")
                continue
            else:
                print("Good password")
    break
