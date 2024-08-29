"""
File: Prog9Russo.py

This will define the Item class

"""

class Item:

    """This class represents an how many items are in the list, what each item is, the quantity of each item and price"""


    def __init__(self, name, quantity, price):

        self.myName= name

        self.myQuantity= quantity

        self.myPrice= price

    def __str__(self):

        """Returns the string representation of the item object"""

        result = "Name: " + self.myName + "\n"

        result += "Quantity: " + str(self.myQuantity) + "\n"

        result += "Price: $" + str(self.myPrice) + "\n"

        return result

    def getName(self):

        """Returns the name"""

        return self.myName

    def getQuantity(self):

        """Returns the quantity"""

        return self.myQuantity

    def getPrice(self):

        """Returns the price"""

        return self.myPrice

    def setName(self, name):

        """Sets the name"""

        self.myName= name

    def setQuantity(self, quantity):

        """Sets the quantity of the item"""

        self.myQuantity = quantity

    def setPrice(self, price):

        """Sets the price of the items"""

        self.myPrice= price
        

    

        
 

        

        
        
