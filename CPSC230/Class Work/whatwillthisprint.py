#1
i=input("Please give me characters ")
b=list(i)
b.sort()
c="".join(b)
print(c)
#2
finallist = []
all = ['apple', 'Banana', 'orange', 'Mango', 'grapes', 'strawberry', 'kiwi' , 'Apricot']
vstring = "aeiou"
vlist = ['a', 'e', 'i', 'o', 'u']
for i in all:
    if i[0].lower() in vstring:
        finallist.append(i)
print(finallist)
