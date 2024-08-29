## Julianna Russo
##
## Prog3Russo.py
##
## Purpose: this program will calculate a buyers total net payment along with the service charge and tax calculation for the amount of songs they bought
##
## Input: the inputs will be the buyers first and last name, number of songs purchased and the price per song 
##
## Output: the buyer's full name, number of songs purchased, price per song, service charge, taxess owed, and the total charge
##
## Certification of Authencity: I certify that this lab is entirely my own work

def main():

    numSongs=0

    costPerSong= 0
    #Initalizes both the numSongs variable and the costPerSong variable to 0
    
    print("Hello, this program will calculate what you will be paying for the song you downloaded")
    #Greets the user and gives a breif description of what the program does

    lastName= input("Please enter your last name: ")

    firstName= input("Please enter your first name: ")

    costPerSong=float(input("Please enter the cost per song: $"))

    numSongs= int(input("Please enter the number of songs downloaded: "))

    baseCharge= numSongs * costPerSong
    #calculates the base charge
    
    if numSongs <=5:
    #if the number of songs is 5 or less the service charge will be 11%
        serviceChargeCalculation= .11 

    elif numSongs< 8:
    #if the number of songs is more than 5 but less than 8 the service charge will be 9%
        serviceChargeCalculation= .09

    else:
    #if the number of songs is 8 or more the service charge will be 6%
        serviceChargeCalculation= .06
        
    serviceCharge= serviceChargeCalculation * baseCharge

    roundedServiceCharge= round(serviceCharge , 2)
    #rounds the service charge to the second decimal place

    netPayment= serviceCharge + baseCharge
    #The net payment is the sum of the service charge and the base charge

    if netPayment <= 4.00:
    #if the net payment is less than or equal to $4, the tax rate is 0%
        taxRate= 0

    elif netPayment <= 7.50:
    #if the net payment is greater than $4 but less than or equal to $7.50, the tax rate will be 3.5%
        taxRate= 0.035

    elif netPayment <= 10.99:
    #the tax rate is 7.75% if the net payment is greater than $7.51 and less than or equal to $10.99
        taxRate= 0.0775

    else:
    #any other values of the net payment will have the tax rate at 9%
        taxRate=0.09

    tax= netPayment * taxRate

    roundedTax=round(tax,2)
    #calculates the tax, then rounds it off to the 2nd decimal place

    totalCharge= tax + netPayment

    roundedTotalCharge=round(totalCharge,2)
    #calculates the total charge, and rounds it to the 2nd decimal place

    fullName= firstName + " " +lastName

    print("Full name is:",fullName)

    print("The number of songs pruchased is:", numSongs)

    print("The price per song is: $" ,costPerSong)

    print("The service charge is: $" ,roundedServiceCharge)

    print("The tax owed is: $" ,roundedTax)
    
    print("Your total charge is: $" ,roundedTotalCharge)

    #Returns: the user's first and last name, the number of songs, the cost per song, the service charge rounded to the 2nd decimal place
    #Returns: the tax rounded to the 2nd decimal place, and the total charge rounded to the second decimal place

    print("Thank you! Have a nice day")
    #a goodbye to the user
main()
