#Ananya and Zach
priceDict = {}
calorieDict = {}
stockDict = {}
#making inventory function
def inventoryGenerator():
    while(True):
        try: #inputting keys and values into respective dictionaries
            name = input("Please give me the name of the candy ")
            nameInput=name.lower()
            priceInput = float(input("Please give me the price for this candy "))
            calorieInput = int(input("Please give me how many calories this is "))
            stockInput = int(input("Please give me the stock of this candy "))
            priceDict[nameInput]=priceInput  #inputting the inputs into the dictionaries
            calorieDict[nameInput]=calorieInput
            stockDict[nameInput]=stockInput
        except ValueError: #accounting for if there was an incorrect input by the user
            print("One of these values is invalid. Please input your item's information again correctly.")
            continue
        newEntry = input("would you like to input another item? ")   #asking user if they want multiple entries
        if(newEntry.lower() == "yes"):  #asking for multiple entries
            continue
        else:
            break
#making purchase function
def makePurchase():
    purchase = input("What would you like to buy? ").lower()
    hasItem = False
    for i in stockDict:
        if(i == purchase):
            hasItem = True
    if(hasItem == True):
        quantity = int(input("Perfect! How many would you like to buy? "))
        if quantity <= stockDict.get(purchase):
            totalPrice = quantity*priceDict.get(purchase)  #calculating price and calories of purchase
            totalCalories = quantity*calorieDict.get(purchase)
            print("Fantastic!")
            stockDict[purchase]=stockDict.get(purchase) - quantity  #changing the quantity in the inventory
            return [purchase, totalPrice, quantity, totalCalories]

        else:
            print("We only have", stockDict.get(purchase))   #if they ask for too many items
    else:
        print("We don't carry that candy. Please try again.")   #if user asks for nonexistent item
#sell function
def sell():
    billItems = []
    while(True):
        userInput = input("Would you like to buy an item? ")   #running purchase function for more items
        if(userInput.lower() == "yes"):
            billItems.append(makePurchase())
        else:
            print("Thank you for shopping with us today! Here is your receipt.")
            print("The receipt reads...")
            for i in billItems:
                print(i[0],": ", "$",i[1],", ","#",i[2],", ","cal-",i[3])    #printing final receipt
            break
inventoryGenerator()
sell()
