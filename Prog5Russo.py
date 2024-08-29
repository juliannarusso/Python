## Julianna Russo
##
## Prog5Russo.py
##
## Purpose: the purpose of this program is to use information from a file to calculate tax information
##
## Input: the input used in this program is the name of the text file
##
## Output: the output of this program is the number of tax payers and each tax payer's ID, filing status, taxable income, tax rate, and tax amount owed
##         The program will also output the highest tax amount paid, the ID of the person who paid the most in taxes, the total amount of taxes paid, and the average tax amount
##
## Certification of Authenticity: 
##
## I certify that this program is entirely my own work


def main():

    highestTax=0

    averageTax=0

    totalTax=0
    #Sets constants to 0 so they can be used ater in the code
    print("Hello, this program will promt for a file and use the information in the file to compute the tax information for each person useing the program ")

    fileName= input("Enter file name please: ")
    #Gets the file name
    theFile= open(fileName, 'r')

    line= theFile.readline()

    numInputs=int(line)
    #gets the number of users that will be using this program

    for i in range(numInputs):
        ##this parameter is the number of people using this program, so it will loop a certian amount of times
        taxID= theFile.readline()

        intTaxID= int(taxID)
        #this converts the tax ID into an int
        print("Your tax Id is:",intTaxID)

        status= theFile.readline().strip()
        #this strips the string of excess white space and this will be the filing status
        filingStatus= str(status)

        if filingStatus =="S" or filingStatus=="s":

            fStatus= "Single"
            #this allows for a uppercase and a lowercase letter to be used and prints out the word not just the letter

        elif filingStatus=="M" or filingStatus=="m":

            fStatus="Married filing Jointly"

        else:

            fStatus= "Head of Household"
            
        print("Status is:",fStatus)

        grossIncome= theFile.readline()

        floatGross= float(grossIncome)
        #converts the gross incomme into a float

        numExempt=theFile.readline()

        intExempt=int(numExempt)

        exemptions=intExempt* 1500

        taxableIncome= (floatGross-4000)-exemptions
        #calculates the taxable income

        roundedTaxIncome=round(taxableIncome,2)
        #rounds the taxable income to the second decimal place

        print("Your taxable income is: $",roundedTaxIncome)

        if filingStatus == "s" or filingStatus=="S":
        #this loop will determine the tax rate based on the taxable income and the filing status
            if taxableIncome<0:

                taxRate=0
                taxableIncome=0.00
                #If the taxable icome is less than 0 there is no taxes owed and no tax rate

            elif taxableIncome< 15000:

                taxRate= 0.14

            elif taxableIncome<=30000:

                taxRate= .20

            else:
                taxRate= .31

        elif filingStatus=="m" or filingStatus=="M":
            #allows for an uppercase and lowercase m to be usedd and bases the tax rate based off filing status and the taxable income

            if taxableIncome<0:

                taxRate=0
                taxableIncome=0.00
                #if taxable income is less than 0 then there is no taxable income and no tax rate

            elif taxableIncome<20000:

                taxRate= .15

            elif taxableIncome <=65000:

                taxRate= .2

            else:

                taxRate=.27

        else:

            if taxableIncome< 0:

                taxRate= 0
                taxableIncome=0.00
                #if taxable income is less than 0, there is no taxes owed and no tax rate

            elif taxableIncome <30000:

                taxRate=.13


            elif taxableIncome<=85000:

                taxRate= .21

            else:

                taxRate=.3

        print("Tax rate is:",taxRate*100,"%")
        #prints out the tax rate

        taxOwed= taxableIncome * taxRate

        roundedTaxOwed=round(taxOwed,2)
        #computes the taxes owed and then rounds it to the second decimal place

        print("Total taxes owed is: $",roundedTaxOwed)

        averageTax= taxOwed+averageTax
        #keeps track of the taxes added together so the average can be totaled up at the end

        if taxOwed> highestTax:
            #keeps track of the highest tax paid and the taxpayer ID that pays the highest amount

            highestTax= roundedTaxOwed

            highestTaxID= taxID

        totalTax=taxOwed+totalTax

        roundedTotalTax=round(totalTax,2)
        #rounds the total taxes owed to the second decimal place

    print("There are",numInputs,"people using this program")

    totalAverageTax= averageTax/numInputs

    roundedAverageTax=round(totalAverageTax,2)
    #rounds the average taxes to the second deccimal place

    print("Tax payer",highestTaxID.strip(),"paid the most in taxes at $",highestTax)

    print("The total amount of taxes paid is: $",roundedTotalTax)

    print("The average tax aount is: $",roundedAverageTax)

    print("Thank you, have a nice day!")
    #returns the highest tax amount, the ID the corresponds with the highest tax amount, the average tax amount, the amount of users, the tax rate, taxable income,
    ##  The filing status, and the total amount of taxes paid
    theFile.close()
    #closes the file

main()
