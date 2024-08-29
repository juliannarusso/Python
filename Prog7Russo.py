## Julianna Russo
##
## Prog7Russo.py
##
## Purpose: The purpose of this program is to have the user choose what they want from the menu, then based off their choice they will wither
##          handle grades, calculate if there are more positive or negative numbers, how many times a certian numer appears in an array
##          grade a quiz and to quit they will type 'Q'. The menu will loop until the user presses Q.
##
## Input: the user will input their menu choice, then based off their menu choice they will input different data for different functions.
##      For the handling grades menu choice the input will be 5 integers, the More positives or negatives will input up to 10 floats
##      For the 'How Many Times' menu choice the user will input up to 10 negative intergers, and a target value
##      For the 'Grade a Quiz' menu choice the user will input 12 answers a student choose on a quiz, and then the correct answer choices
##
## Output: The output is different for each menu choice. The output for the 'Handling Grades' menu choice is the highest grade, lowest grade, and average grade
##      The output for the 'More positives or More Negatives' will be if there are more positive or negative numbers in the array, along with printing out only the numbers that are positive or negative based on which has more. In a tie the output will be the entier array with the message that there was a tie
##      The output for 'How Many Times' is the the array, the target value, and how many times the target value occurs in the array
##      The output for 'Grade a Quiz' is the student's quiz grade as a percentage and as a corresponding letter grade
##      The output for 'Quit' iis the message "Thank you! Goodbye!"
##
## Certification of Authencity: I certify that this lab is entirely my own work


def main():
    print("Hello, this program give you, the user, a varity of menu options to choose from, and will continue to give them to you until you press Q")

    choice= -1

    while (choice!= 'Q' and choice != 'q'):

        print("H- Handling Grades")

        print("M- More Positives or More Negatives")

        print("T- How Many Times")

        print("G- Grade a Quiz")

        print("Q- Quit")

        choice= input("Please enter the your choice: ").strip()

        if (choice== 'Q' or choice=='q'):

            print("Thank you! Goodbye")

        elif( choice== 'H' or choice=='h'):

            handleGrades()

        elif( choice== 'M' or choice=='m'):

            morePositivesOrNegatives()

        elif( choice== 'T' or choice=='t'):

            print("call T")

            howManyTimes()

        elif( choice== 'G' or choice=='g'):

            print("call g")

            gradeQuiz()

        else:

            print("Sorry, that isn't a valid choice")



def gradeQuiz():

    ##This function will grade a students quiz by collecting the student's answer choice and comparing that to the correct answer provided by the user

    print("Hello, this choice will be asking you for 12 choices a student choose for a multiple choice quiz, then ask for the 12 correct answers, then the student's grade will be calculated.")

    studentAnswer=[]

    correctAnswer=[]

    questionNumber=0

    theQuestionNumber=0

    for i in range(12):

        questionNumber=questionNumber+1

        questionNumberString=str(questionNumber)

        ##converts the question number into a string 

        studentChoice=input("Please enter the student's answer for question "+questionNumberString+" using A,B,C, and D: ").strip()

        while studentChoice!='A' and studentChoice!= 'B' and studentChoice!= 'C' and studentChoice!= 'D':

            studentChoice=input("Please enter the student's answer for question "+questionNumberString+" using A,B,C, and D: ").strip()
            
        studentAnswer.append(studentChoice)

        ##adds the answer to the list

    for i in range(12):

        theQuestionNumber=theQuestionNumber+1

        theQuestionNumberString=str(theQuestionNumber)

        ##converts the question numer into a string

        correctChoice=input("Please enter the correct answer for question "+theQuestionNumberString+" using A,B,C, and D: ").strip()

        while correctChoice!='A' and correctChoice!='B' and correctChoice!='C' and correctChoice!='D':

            correctChoice=input("Please enter the correct answer for question "+theQuestionNumberString+" using A,B,C, and D: ").strip()
            
        correctAnswer.append(correctChoice)

    gradeQuizAnswer(studentAnswer,correctAnswer)

    print(gradeQuizAnswer(studentAnswer,correctAnswer))

    return(gradeQuizAnswer(studentAnswer,correctAnswer))

    ##Returns the students quiz grade

def gradeQuizAnswer(studentAns,correctAns):

    ##The purpose is to grade the students quiz and return the numeric grade along with the corresponding letter grade

    numCorrectAns=0

    for i in range(len(studentAns)):

        if studentAns[i] == correctAns[i]:

            ##Will loop if the student got the correct answer

            numCorrectAns=numCorrectAns+1

    numGrade= numCorrectAns/12

    percentGrade= numGrade*100

    if percentGrade<=59.99:

        letterGrade='F'

    elif percentGrade<=64.99:

        letterGrade='D'

    elif percentGrade<=67.99:

        letterGrade='D+'

    elif percentGrade<=69.99:

        letterGrade='C-'

    elif percentGrade<=74.99:

        letterGrade='C'

    elif percentGrade<=77.99:

        letterGrade='C+'

    elif percentGrade<=79.99:

        letterGrade='B-'

    elif percentGrade<=84.99:

        letterGrade='B'

    elif percentGrade<=87.99:

        letterGrade='B+'

    elif percentGrade<=89.99:

        letterGrade='A-'

    else:

        letterGrade='A'

    theGrades= "The stundet's letter grade is: "+letterGrade + "  The grade percent is: {0:0.2f}".format(percentGrade)+"%"

    ##'theGrades' will make it easy to return the information of the quiz grade to the user

    return theGrades

    ##returns the letter and number grade


def howManyTimes():

    ##This program will ask for up to ten negative numbers, and puts them in a list, the user will then be asked for a target value

    count=0

    numberList=[]

    numbers=-9999999

    print("This choice will have you enter up to 10 negative values, entering a non negative value will mean you are finished entering data.")

    while numbers<0 and count<10:

        numbers=int(input("Please enter a negative number: "))

        if numbers<0:

            numberList.append(numbers)
    
            count=count+1

    targetValue=int(input("Please enter a target value: "))

    countTargetValue(numberList,targetValue)

    

def countTargetValue(numList,theTarget):

    ##The parameters is the number list and the target value
    ##This program will count up the amount of times a target value appears in an array

    count=0

    for i in range(len(numList)):

        if numList[i]== theTarget:

            count=count+1

    print("The array is",numList)

    print("The target value is",theTarget)

    print("The amount of times the target value appears in the array is",count,"times")    
    


def morePositivesOrNegatives():

    ##This function will prompt the user for at most ten numbers, entering a 0 will indicate that the user is done adding numbers into the list

    theNums=[]

    print("This choice will have you enter values up to ten times and tell you if you entered more positive or negative numbers. Enter 0 to stop")

    count=0

    numbers= float(input("Please enter a positive or negative number: "))

    while count<10 and numbers!=0:

        theNums.append(numbers)

        count=count+1

        numbers= float(input("Please enter a positive or negative number: "))

    countPositivesAndNegatives(theNums)

    return(theNums)

def countPositivesAndNegatives(nums):

    ## this parameter is the 'theNums' list from the morePositivesOrNegatives function
    ## this function will datermine if there are more postives or negatives in the list and print out the answer, along with the corresponding array
    ## If there are an equal amount of positive and negative number the function prints the entire array along with a message saying that it is a tie
    countPositive=0

    countNegative=0

    answer="There are more positive numbers than negative numbers"

    positiveNums=[]

    negativeNums=[]

    for i in range(len(nums)):

        if nums[i] > 0:

            countPositive=countPositive+1

            positiveNums.append(nums[i])
            
        if nums[i] <0:

            countNegative=countNegative+1

            negativeNums.append(nums[i])

    if countPositive<countNegative:

        answer="There are more negative numbers than positive numbers"

        print(negativeNums)

        print(answer)

    if countPositive>countNegative:
        
        print(answer)

        print(positiveNums)
                
    if countPositive==countNegative:

        answer="There are the same amount of positive and negative numbers"

        print(answer)

        print(nums)
    
    return answer

    ## The function will return the answer

    

def handleGrades():

    ##This function takes in 5 grades then returns the lowest grade, highest grade and the average grade

    grades=[]

    print("This program will now ask you for 5 grades, then give you the highest grade, lowest grade, and the averge grade.")

    for i in range (5):

        theGrade= int(input("Please enter the numeric grade: "))

        while theGrade <0 or theGrade>100:

            print("Sorry, that is not a valid grade. Please enter a valid grade.")

            theGrade= int(input("Please enter the numeric grade: "))

        grades.append(theGrade)
    
    maxGrade(grades)

    minGrade(grades)

    averageGrade(grades)

    print("The highest grade was a",maxGrade(grades))

    print("The lowest grade was a", minGrade(grades))

    print("The average grade is a",averageGrade(grades))

    return(grades)


def maxGrade(theGrades):

    ##The purpose of this funstion to to find the highest grade

    ##The parameter 'theGrades' is the list 'grades' in the handleGrades function

    maxGrade=theGrades[0]


    for i in range(len(theGrades)):

        if theGrades[i]> maxGrade:

            maxGrade= theGrades[i]

    return maxGrade

    ##Returns the maximum grade


def minGrade(theGrades):

    ##The purpose of this function is to determine the lowest grade

    ##The parameter 'theGrades' is the list 'grades' in the handleGrades function

    minGrade=theGrades[0]

    for i in range(len(theGrades)):

        if theGrades[i]< minGrade:

            minGrade= theGrades[i]

    return minGrade

    ##The function returns the lowest grade

def averageGrade(theGrades):

    ##The parameter 'theGrades' is the list 'grades' in the handleGrades function

    theSum=0

    for i in range(len(theGrades)):

        theSum=theSum+theGrades[i]

    theAvg= theSum/5

    return(theAvg)

    ##Returns the average of the grades
    



main()
    
