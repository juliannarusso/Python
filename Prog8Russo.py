## Julianna Russo
##
## Prog8Russo.py
##
## Purpose: The purpose of this function is to take values from the user and draw a rectangle with those values. The class Rectangle is take from a seperate file and I imported it so it can be used.
##
## Input: The input is the fill style, the width of the rectangle, the height of the rectangle, and the menu choice
##
## Output: This program will output the area, the perimeter, the text description of the rectangle, the rectangle itself, the fill style,and the height and width of the rectangle
##
## Certification of Authencity: I certify that this lab is entirely my own work
##

from RectangleRusso import Rectangle

def main():

    theRectangle= Rectangle(-9999,-9999," ")

    ##This sets the values of the rectangle width, height, and the fill style so there is an easier change

    print("Hello! Lets build a rectangle!!")

    choice = -0

    while (choice != "Q"):

        ##This will loop until the user quits the program

        print("Please enter your choice")

        print("W : Assign the Width")

        print("H : Assign Height")

        print("F : Assign Fill Style")

        print("A : Calculate Area")

        print("P : Calculate the Perimeter")

        print("T : Text Description of the Rectangle")

        print("D : Draw the Rectangle")

        print("O : Draw Outline")

        print("Q : Quit")

        choice= input("Please enter your choice: ").strip()

        if (choice== "Q" or choice == "q"):

            print("Thank you! Good bye")

        elif (choice == "W" or choice == "w"):

            myWidth= int(input("Please enter a value for the width: "))

            while myWidth <=0:

                ##This will loop until the user inputs a valid value for the width, then sets the width in the rectangle

                print("Sorry, that value isn't valid. Please enter a number greater than 0 for the width")

                myWidth= int(input("Please enter a value greater than 0 for the width: "))

            theRectangle.setWidth(myWidth)

        elif (choice == "H" or choice =="h"):

            myHeight= int(input("Please ener a value for the height: "))

            while myHeight<=0:

                ##Loops on bad data till a valid input for the height is given

                print("Sorry that isn't a valid value for the height")

                myHeight= int(input("Please enter a value greater than 0 for the height: "))

            theRectangle.setHeight(myHeight)

        elif (choice == "F"or choice =="f"):

            myFillStyle = input("Please enter a character for your fill style: ").strip()

            theRectangle.setFillStyle(myFillStyle)

            ##This doesn't need a while loop because it is a string

        elif (choice == "A" or choice=="a"):

            ##The if loops are there to make sure there is a height and width for the rectangle, so the program won't crash.

            if (theRectangle.getHeight() == -9999):

                print("A value for the height is needed")

                myHeight= int(input("Please ener a value for the height greater than 0: "))

                theRectangle.setHeight(myHeight)

            if (theRectangle.getWidth() == -9999):

                print("A value for the width is needed")

                myWidth= int(input("Please enter a value greater than 0 for the width: "))

                theRectangle.setWidth(myWidth)

            ##This will calculate the area of the rectangle

            calcArea(myHeight, myWidth)

            print("The area of this rectangle is", calcArea(myHeight, myWidth))

        elif (choice== "P" or choice =="p"):

            ##The if loops will ensure that if there is no value for the height or the width, this program will not crash.

            if (theRectangle.getHeight() == -9999):

                print("A value for the height is needed")

                myHeight= int(input("Please ener a value for the height greater than 0: "))

                theRectangle.setHeight(myHeight)

            if (theRectangle.getWidth() == -9999):

                print("A value for the width is needed")

                myWidth= int(input("Please enter a value greater than 0 for the width: "))

                theRectangle.setWidth(myWidth)

            ##The perimeter will be calculated once all the necessary information is provided

            calcPerimeter( myHeight, myWidth)

            print("The perimeter of this rectangle is", calcPerimeter( myHeight, myWidth))

        elif (choice == "T" or choice =="t"):

            theRectangle.getHeight()

            print("This rectangle's length is :", theRectangle.getHeight())

            theRectangle.getWidth()

            print("This rectangle's width is :", theRectangle.getWidth())

            theRectangle.getFillStyle()

            print("This rectangle's fill style is :", theRectangle.getFillStyle())

            print("The area of this rectangle is :", calcArea(myHeight, myWidth))

            ##Since there is nothing in the imported file about the area or perimeter, i cannot use a getter

            print("The perimeter of this rectangle is :", calcPerimeter(myHeight, myWidth))

        elif(choice == "D" or choice =="d"):

            ##The if loop is here to ensure all the necessary information is present for the program to draw a rectangle, otherwise the program could crash

            if(theRectangle.getFillStyle()==" "):

                print("A fill style is needed.")

                myFillStyle = input("Please enter a character for your fill style: ").strip()

                theRectangle.setFillStyle(myFillStyle)

            if (theRectangle.getHeight() == -9999):

                print("A value for the height is needed")

                myHeight= int(input("Please ener a value for the height greater than 0: "))

                theRectangle.setHeight(myHeight)

            if (theRectangle.getWidth() == -9999):

                print("A value for the width is needed")

                myWidth= int(input("Please enter a value greater than 0 for the width: "))

                theRectangle.setWidth(myWidth)

                ##The drawRectangle method will use the fill style, width and height values to draw a rectangle

            drawRectangle(myFillStyle, myHeight, myWidth)

        elif(choice =="O" or choice =="o"):

            ##The if loop is here to ensure all the necessary information is present for the program to draw a rectangle, otherwise the program could crash

            if(theRectangle.getFillStyle()==" "):

                print("A fill style is needed.")

                myFillStyle = input("Please enter a character for your fill style: ").strip()

                theRectangle.setFillStyle(myFillStyle)

            if (theRectangle.getHeight() == -9999):

                print("A value for the height is needed")

                myHeight= int(input("Please ener a value for the height greater than 0: "))

                theRectangle.setHeight(myHeight)

            if (theRectangle.getWidth() == -9999):

                print("A value for the width is needed")

                myWidth= int(input("Please enter a value greater than 0 for the width: "))

                theRectangle.setWidth(myWidth)

            drawOutline(myFillStyle, myHeight, myWidth)

        else:

            ##If the user doesn't input a valid menu choice, they will be prompted to choose one again

            print("Sorry, that isn't a valid choice. Please enter a valid option")


def drawOutline(theFillStyle, theHeight, theWidth):

    ##The purpose of this method is to draw the outline of the rectangle

    ##The parameter theFillStyle holds the myFillStyle value

    ##The parameter theHeight holds the value of myHeight, that the user input

    ##The paramteter theWidth hold the value of the width the user has already input

    height= theHeight -2

    ##for printing the outline of a rectangle, the height needs to be subtracted by 2 so the middle of the rectangle can be empty

    topBottomLine=(theFillStyle+ " " ) * theWidth

    ##topBottomLine will create the top and bottom sides of the rectangle, since they will be used in the outline

    numSpaces= (theWidth + theWidth)-3

    ##numSpaces is the number I needed to multiply " " by in order to make the rectangle empty while will having both right and left siide be filled out

    lines= (" " * numSpaces )

    print(topBottomLine)

    for i in range(height):

        print(theFillStyle + lines + theFillStyle)

        ##This willcreate the actual outline of the rectangle

    print(topBottomLine)

    ##This method won't return anything but it will print out the rectangle outline
    

def drawRectangle(theFillStyle, theHeight, theWidth):

    ##The purpose of this method is to draw the rectangle using the fill style
    
    ##The parameter theHeight hold the value the user input for the height

    ##The parameter theWidth holds the value the user input for the width

    ##The pparameter theFillStyle, hold the value for myFillStyle 

    lines=  (theFillStyle+ " " ) * theWidth

    for i in range(theHeight):
        print(lines)

    ##Doesn't return anything, but does print out the rectangle


def calcPerimeter(heightValue, widthValue):

    ##Purpose is to use the length and width to calculate the perimeter

    ##The parameters are the value of the length of the rectangle and the value for the width of the rectangle

    ##The parameter heightValue hold the value the user input for the height

    ##The parameter widthValue holds the value the user input for the width

    perimeter= 0

    perimeter= (heightValue * 2) + ( widthValue *2)

    return perimeter

    ##This returns the value of the perimeter


def calcArea(heightValue, widthValue):

    ##Purpose is to calculate the area of the rectangle using the length and width values

    ##The parameter heightValue hold the value the user input for the height

    ##The parameter widthValue holds the value the user input for the width

    area=0

    area= heightValue * widthValue

    return area

    ##This returns the area value 


main()




              
