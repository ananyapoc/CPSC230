#asking for user input
m=int(input("what month were you born in?"))
d=int(input("what day were you born?"))
y=int(input("what year were you born in?"))

print((2019-y)*365*30*24*60*60 + (9-m)*30*24*60*60 + (5-d)*24*60*60)
