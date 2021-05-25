#this is to calculate a given amount of seconds into its respective hours, minutes, and seconds
a=int(input("please give me a number between 1 and 86,400 :")) #asking for user input
a//3600 #this is to find how many whole hours
b=int((a//3600)) #defining b as hours
b*3600 #this is to find how many seconds the hours are
a-(b*3600) #this is to find how many seconds are left (remainder)
c=int(a-(b*3600)) #defining c as remainder
c//60 #this is to find how many whole minutes
d=int(c//60) #defining d as minutes
d*60 #this is to find how many seconds the minutes are
c-(d*60) #this is to find how many seconds are left (remainder)
e=int(c-(d*60)) #definning e as seconds
print(a , "seconds is equivalent to" , b , "hours" , d , "minutes" , "and" , e , "seconds")
