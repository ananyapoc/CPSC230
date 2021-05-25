dict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
userInput = input("Please give me an operation to complete ")
userList = userInput.split(" ")
if "plus" in userList:
    answer = dict[userList[0]] + dict[userList[2]]
    print(answer)
elif "minus" in userList:
    answer = dict[userList[0]] - dict[userList[2]]
    print(answer)
elif "times" in userList:
    answer = dict[userList[0]] * dict[userList[2]]
    print(answer)
