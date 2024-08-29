##
## Julianna Russo
##
## Prog6Russo.py
##
## Purpose: this program will calculate the cost of the movies each customer buys including service charge, tax and will then print out a summary describing their purchase
##
## Input: the customer ID, the customer name, and the number of movies ordered
##
## Output: Customer name,cutomer ID, Number of ovies purchased,total cost of the movies, service charge, total amount due, number of customers, highest amount charged
##      customer ID with the highest amount charged, lowest amount charged and the ID that corresponds, the total combined dollar amount of all movies purchased, and the average
##
## Certification of Authenticity: I certify that this lab is entirely my own work
##                              
def main():

    countCustomers=0

    highestCharge=-9999999999999999999999

    highestChargeId=-9999999999999999999

    lowestCharge=9999999999999999999999

    lowestChargeId=99999999999999999999

    totalAmountAll=0

    theAverage=0

    ##Sets constants so the values can be replaces later in the function

    print("This program will FIX THIS LATER!!!")

    customerId=int(input("Please enter your customer ID: "))

    while(customerId!=0):

        ##will loop on bad data

        customerName=input("Please enter your name: ").strip()

        numMovies=int(input("Please enter the number of movies you ordered: "))

        while numMovies<=0:
            ##Loops on bad data

            print("Sorry, no negatives allowed.")

            numMovies=int(input("Please enter the number of movies you ordered: "))

        movieAmount=chooseMovies(numMovies)

        serviceChargeAmount=calcServiceCharge(numMovies,movieAmount)

        theTotalDue=calcTotalDue(movieAmount,serviceChargeAmount)

        outputtingResults=outputResults(customerName,customerId, numMovies,movieAmount,serviceChargeAmount,theTotalDue)

        countCustomers=countCustomers=countCustomers+1
        ##Keeps track of how many customers use this program

        if theTotalDue>highestCharge:

            highestCharge=theTotalDue

            highestChargeId=customerId

        if theTotalDue<lowestCharge:

            ##keeps track of the lowest charge and the id that corresponds with it

            lowestCharge=theTotalDue

            lowestChargeId=customerId

        totalAmountAll=totalAmountAll+ theTotalDue

            
        customerId=int(input("Please enter your customer ID: "))

    if countCustomers==0:

        ##if the number of customers is 0, the program won't crash

        theAverage=0

    else:

        theAverage= totalAmountAll/countCustomers

    print("Thank you, have a nice day")

    print("There were",countCustomers,"people using this program")

    print("The highest charge was, ${0:0.2f}".format(highestCharge))

    print("The customer ID with the highest charge is:",highestChargeId)

    print("The lowest charge was, ${0:0.2f}".format(lowestCharge))

    print("The customer ID with the lowest charge was:",lowestChargeId)

    print("The total dollar amount of all the movies purchased is, ${0:0.2f}".format(totalAmountAll))

    print("The average for all the purchased amounts is, ${0:0.2f}".format(theAverage))
    ##The final summary for the program, will print a summary of all the given data information and formats it nicely

def chooseMovies(numberMovies):
    ##this function calculates the cost of all of the movies for one cutomer
    ## The parameter holds the number of movies the customer purchased
    allMovieCost=0

    for i in range(numberMovies):

        movieLength= int(input("How long is the movie in minutes(between 1 and 240 inclusively): "))

        if movieLength> 240 or movieLength<1:

            print("Sorry, invalid movie length.")

            movieLength= int(input("How long is the movie in minutes(between 1 and 240 inclusively)"))

        rating= input("Please enter the rating of the movie(G for G-rated, P for PG-rated,R for R-rated, X for X-rated, O for Other): ").strip()

        if rating=="G" or rating=="g":

            costPerMin= .059

        elif rating =="P" or rating=="p":

            costPerMin= .054

        elif rating =="R" or rating=="r":

            costPerMin=.061

        elif rating=="X" or rating =="x":

            costPerMin=.197

        elif rating =="O" or rating =="o":

            costPerMin=.067

            ##Allows for a capital and lowercase letter to be used

        else:

            print("Sorry, that isn;t a vaild rating.")

            rating= input("Please enter the rating of the movie(G for G-rated, P for PG-rated,R for R-rated, X for X-rated, O for Other): ").strip()

        theCost= costPerMin * movieLength

        allMovieCost= allMovieCost + theCost

    return allMovieCost
##Returns the cost of each movie added up

def calcServiceCharge(numberMovies,movieCosts):
##The parameter holds the number of movies purchased and the sum of all the movies purchased by one customer
## This function will calculate the service charge
    if numberMovies <= 0:

        serviceCharge = 0

    elif numberMovies <= 4:

        serviceCharge = .14*movieCosts

    elif numberMovies <= 8:

        serviceCharge = .10*movieCosts

    elif numberMovies <= 11:

        serviceCharge =.075*movieCosts

    else:

        serviceCharge=.04*movieCosts

    return serviceCharge
##This will return the service charge value

def calcTotalDue(movieCosts, serviceChargeCosts):
##The parameter holds the cost of all the movies for one customer, and what the service charge cost is
##This function will calculate the total amount due, including tax
    theSum=movieCosts+serviceChargeCosts

    tax= theSum* .0825

    fullAmount= theSum + tax

    return fullAmount
##Returns the full amount due including tax
    
def outputResults(nameCustomer,IdCustomer,numberMovies,movieCosts,chargeService,totalDue):
##This function will formate and print the customers purchase summary neatly
## the parameters hold the customer name and id, the number of movies purchased, the cost of all the movies purchased, the service charge cost, and the total amount due

    print("Customer name is:", nameCustomer)

    print("Customer ID is:",IdCustomer)

    print("The number of movies purchased:",numberMovies)

    print("The costs of just the movies purchased is: ${0:0.2f}".format(movieCosts))

    print("The service Charge is: ${0:0.2f}".format(chargeService))

    print("The total amount due is: ${0:0.2f}".format(totalDue))



main()
    
