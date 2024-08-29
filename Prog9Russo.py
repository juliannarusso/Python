## Julianna Russo
##
## Prog9Russo.py
##
## Purpose: The purpose of this program is to read in data from a text file and convert that into a shopping list while also allowing the user to make modifications to their shopping list.
##
## Input: The input used is the name of the text file, the menu choice, if the user chooses option 1 the user will input the name, quantity and price of the item they want to add. If the user chooses option 2 they will input the name of the item they want to remove from their cart. If the user chooses 4 they will input the name of the item they want to search for
##
## Output: The output will be the choice the user made for the menu. If the user chose the option 1 the output will be a message that they added an item to their cart. If they choose 2 the output will be a message that they choose to remove a certian item, and if the item isn't in their cart it will let the user know
##        If the user chooses option 3 the output will be all the items in the cart. If the user chooses option 4 the output will be the message if the item is in their cart, and what the quantity and price of that item
##        it the user chooses option 5 the output will the total amount of items in the list. Option 6 outputs the total cost of everything in the users list
##        option 7 will output if the user's list is empty or not. Option 8 outputs a message that tells the user they cleared their list. Option 0 tells the user goodbye
##
## Certification of Authenticity: I certify that this lab is entirely my own work

from ItemRusso import Item

def main():

    itemList= []

    theItem= Item("0",0,0.00)

    print("Hello, this program will track your shopping list for you.")

    fileName= input("Enter file name please: ")

    theFile= open(fileName, 'r')

    line= theFile.readline()

    numInputs=int(line)

    for i in range(numInputs):

        myName= theFile.readline().strip()

        theItem.setName(myName)

        theQuantity= theFile.readline()

        myQuantity= int(theQuantity)

        theItem.setQuantity(myQuantity)
       
        thePrice= theFile.readline()

        myPrice= float(thePrice)

        theItem.setPrice(myPrice)

        aItem= Item(theItem.getName(), theItem.getQuantity(), theItem.getPrice())

        itemList.append(aItem)

    choice= -9999

    while choice != "0":

        print( "1. Add an item to the list")

        print( "2. Remove an item from the list")

        print("3. Print each item in the list")

        print("4. Search for a user-specified item in the list")

        print("5. Count the total number of items in the list")

        print("6. Total the cost of the items in the list" )

        print("7. Determine whether the list is empty")

        print("8. Clear the list")

        print("0. Quit")

        choice= input("Please enter your choice: ").strip()

        ##The program only accepts vaild menu choices

        if choice == "0":

            print("Thank you, have a nice day")


        elif choice == "1":

            print("You choose to add an item to your shopping list.")

            anItem(itemList)

        elif choice == "2":

            print("You chose to remove an item from your cart")

            theKey= input("Please enter the item you'd like to remove from your cart: ").strip()

            remove(itemList,theKey)

        elif choice == "3":

            print("You chose to print each item in your shopping list.")

            printList(itemList)

        elif choice =="4":

            print("You chose to search for a specific item in your list.")

            key= input("Please enter the name of the item you want to look for: ").strip()

            search(itemList, key)

        elif choice == "5":

            print("You chose to count all the items in your shopping cart.")

            count(itemList)

            print("You have",count(itemList),"items in your cart.")

        elif choice == "6":

            print("You chose to total the cost of all your items.")

            theCost(itemList)

            print("The total price of all the items in your cart is ${0:0.2f}".format(theCost(itemList)))

        elif choice =="7":

            print("You chose to determine if your shopping list is empty.")

            isEmpty(itemList)

        elif choice == "8":

            print("You chose to empty your list.")

            emptyAll(itemList)

        else:

            print("Sorry that isn't a valid choice. Please enter a valid option.")

    theFile.close()

def remove(items, target):

    ##The parameter is the item list and the target item the user wants to remove

    ##This function removes a user specified item from the user's shopping list

    ans= 0

    for i in range(len(items)):

        if items[i].getName() == target:

            items.pop(i)

            ans +=1

            ##The item is removed from the cart.

    if ans< 1 :

        print("You do not have that item in your cart")

        ##if the item isn't in the user cart this will print

    else:

        print(target,"was removed from your cart")
        

def emptyAll(items):

    ##This function clears the entire list

    ##The parameter is the item list

    for i in range(len(items)):

        items.clear()

def isEmpty(items):

    ##This function lets the user know if the cart is empty or not

    ##The paramete is the item list

    ans= "Yes, your cart is empty"

    num=0

    for i in range(len(items)):

        num+=1

    if num >0:

        ans= "No, Your cart is not full"

    print(ans)

    
def theCost(items):

    ##The parameter is the item list

    ##The purpose of this function is to calculate the total cost of the items in the users cart

    cost=0

    for i in range(len(items)):

        cost += items[i].getPrice() * items[i].getQuantity()

    return cost

    ##Returns the cost of the items

def count(items):

    ##the parameter is the item list

    ##The function counts the number of tiems in the user's shopping cart

    theSum=0

    for i in range(len(items)):

        theSum+= items[i].getQuantity()

    return theSum

    ##This function returns the som of all the items in the cart


def search(items, word):

    ##This function's parameters are the key word the user wants to search for in their cart, and the item list

    ##The purpose of this function is to search for the item the user wants to look for, and tells the user the price and quantity of the item. If the item isn't in the user's cart, the function will tell the user that

    num=0

    pos= 0

    for i in range(len(items)):

        if items[i].getName() == word:

            num+= 1
            pos= i

    if num>0:

        usedFormatPrice= items[pos].getPrice()

        print("You have", items[pos].getQuantity(), word,"at ${0:0.2f}".format(usedFormatPrice),"each")

    else:

        print("You don't have that item in your cart")


def printList(items):

    ##The parameter is the item list

    ##The function's purpose is to print out each item, along with the item number, quantity and price

    num=0

    for i in range(len(items)):

        num+=1

        print("Item",num,"Name:",items[i].getName())

        print("Item",num,"Quantity:", items[i].getQuantity())

        print("Item",num,"Price: ${0:0.2f}".format(items[i].getPrice()))

        print()

        print()
            
    if num== 0:

        print("Your list is empty")


def anItem(items):

    ##This prompts the user for an item to add to their cart, then validates the price and quantity of the item

    ##The parameter is the item list

    theItem= Item("0",0,0.00)

    myName= input("Please enter the name of the item: ").strip()

    theItem.setName(myName)

    myQuantity= int(input("Please enter the quantity of the item: "))

    while myQuantity < 0:

        ##Loops on bad data

        print("That is not a valid quantity.")

        myQuantity= int(input("Please enter the quantity of the item: "))

    theItem.setQuantity(myQuantity)

    myPrice= float(input("Please enter the unit price for the item: $"))

    while myPrice < 0:

        ##loops on bad data

        print("That is not a valid price")

        myPrice= float(input("Please enter the unit price for the item: $"))

    theItem.setPrice(myPrice)

    aItem= Item( theItem.getName(), theItem.getQuantity(), theItem.getPrice())

    items.append(aItem)

    print(theItem.getName(),"has been added to the cart")


main()

    

            


