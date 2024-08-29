##Celsius to Fahrenheit
## Julianna Russo
## convert.py
##
##Purpose: this program's purpose it to convert tempetures from Celsius to Fahrenheit.

## Input: the inputs of this program will be values of degrees in Celsius
## Output: the output of this program is the tempeture given in celsius converted into fahrenheit
##Certification of Authenticity:
## I certify that this lab is entirely my own work
##


def main():
    #this tells the reader that the program will ask 5 times for a temp in Celsius, then convert it to Fahrenheit
    print("Hello! This program will ask you for a tempertaure in Celsius to convert it into Fahrenheit, 5 times.")
    for i in range(5):
        # the parameter in this function is a 5, which means that this functionwill loop 5 times
        #this program will loop 5 times
        celsius= eval(input("Enter the Temperature in Celsius please. "))
        #this will prompt the user to enter a value in celsius and then that number will be the variable
        

        fahrenheit= (9/5) * celsius +32
        #this will make it so the value of the variable fahrenheit is this equation so that it will convert the temp from celsius to fahrenheit
        #display the output
        print( "The tempature is ", fahrenheit,"degrees Fahrenheit")
        #this will return the temp in fahrenheit 
        # this prints out the tempertaure in fahrenheit for the user
    print("Thank you! Have a nice day!")
        #prints out this conclusin so there is no confusion for when the program is over

main()
        
