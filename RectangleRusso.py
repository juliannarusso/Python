## This is the class  named RectangleRusso
## Has three instance variables. myWidth, which is an integer, myHeight, which is an integer, and myFillStyle, which is a string

"""
File: Prog8Russo.py
"""

class Rectangle:

    """This class represents the dimensions of the rectangle, the width, the height, and the fill style"""
    
    def __init__(self,  width, height, fillStyle):

        self.myWidth= width

        self.myHeight= height

        self.myFillStyle= fillStyle

    def __str__(self):

        """Returns the string representation for a rectangle object"""

        result = "Width:  " + str(self.myWidth) + "\n"

        result += "Height:  " + str(self.myHeight) + "\n"

        result += "Fill style:  " + self.myFillStyle + "\n"

        return result

    def getHeight(self):

        """ Returns the height of the rectangle"""

        return self.myHeight

    def getWidth(self):

        """ Returns the width of the rectangle"""

        return self.myWidth

    def getFillStyle(self):

        """Returns the fill style of the rectangle"""

        return self.myFillStyle

    def setHeight(self, height):

        """Sets the height of the rectangle"""

        self.myHeight= height

    def setWidth(self, width):

        """Sets the width of the rectangle"""

        self.myWidth= width

    def setFillStyle(self, fillStyle):

        """Sets the fill style of the rectangle"""

        self.myFillStyle = fillStyle

    
                 
