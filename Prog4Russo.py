##Prog4Russo
##
##Julianna Russo
##
##Purpose: this is a game where the user will have a playing pot of money at the beginning of the game, two dice rolled by the program, and if those two dice add up to 8, the player wins $2, and if they roll ttwo numbers that sum up to 4 or 5 they will win $1, but any other value will make them lose $1. This game will continue till the money runs out. When the program is done the program will print out how many rolls it took for the money to have run out, and the maximum value in the pot
##
##Input: amount of money the user wants to bet
##
##Output: Maximum value of the pot, number of rolls it took for the player to run out of money, the play number that had the most money in the pot, number of rolls, values for dice 1 and dice 2, the amount of money in th epot
##
##Certification of Authenticity: I certify that this lab is entirely my own work
##
##I did the challenge

def main():

    from random import randrange
    #allows for the program to generate random numbers

    print("Hello! Welcome to Poughkeepise 8-4-5!")

    print("Roll two numbers that add up to 4 or 5 and you win $1")

    print("Roll two numbers that add to 8, you win $2")

    print("Roll any different values, you lose $1")
    #gives the user a breif description of what the program does

    numRolls= 0

    maxVal=0

    playNum=0

    numRollsMaxPot=0
    #sets the values to 0

    potNum= int(input("Please enter the amount of money you want to bet(must be between $1-$50 inclusivley): $"))
    #prompts user for how much money they want to bet
    
    while potNum > 50 or potNum < 1:
        #will continue looping if the user enters an invalid value

        print("Sorry, invalid value. ")

        potNum= int(input("Please enter a number between $1-$50 inclusivley: $"))
        #prompts the user for a new pot number value
    while potNum>= 1:

        numRolls= numRolls +1
        #Keeps track of rolls

        dice1= randrange(1,7)
        
        dice2= randrange(1,7)
        #gets a random dice value
        #Parameters for the dice values are 1 up to 7, so the random values will be 1 up to 7

        diceVal= dice1 + dice2
        #adds both dice values up
        
        if diceVal ==8:
            
            potNum= potNum +2
            #adds 2 to the pot value

        elif diceVal== 4 or diceVal==5:
            
            potNum= potNum + 1
            #adds 1 to the pot value

        else:
            
            potNum= potNum - 1
            #subtracts 1 from the pot value

        if potNum > maxVal:
            #to keep track of the max value

            maxVal= potNum
            #sets the max value to the pot number 

            numRollsMaxPot= numRolls
            #keeps track of the play where the pot had the most money
            
        print("Play",numRolls, "  Die 1:",dice1,"  Die 2:",dice2, "  Pot: $",potNum)
        #Returns the play number, the values for both dice values, and the pot number for each play
    print("After", numRolls," plays you are out of money.")

    print("The most amount of money you had in the pot was: $",maxVal)

    print("You had the most money in the pot was in play",numRollsMaxPot)
    
    print("Thank you for playing!")

main()
        
