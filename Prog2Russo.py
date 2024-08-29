##Julianna Russo
##Prog2Russo.py
##Purpose: the purpose of this program is to calculate the score for a promoted tweet which will determine how close to the top it is on the search result
##input: the input will be the number of retweets and replies a tweet gets, and how many days since the tweet first appeared
##output: the output will be the retweet score, the reply score, the day score, and the total score
##  Certification of Authenticity:
## I certify that this lab is entirely my own work

def main():
    print("Hello! This program will compute the total score of a tweet's popularity. The higher the total score is, the more popular the tweet is.")
    #this will greet the user and give them a basic run down about what this program will do
    reTweets= int(input("Please enter the number of re-tweets this tweet has: "))
    #prompts the user for the amount of retweets a tweet gets
    replies= int(input("Please enter the number of replies this tweet has: "))
    #prompts the user for the amount of replies the tweet got
    numDays=int(input("Please enter the number of days the tweet has been posted: "))
    #prompts the user for the amount of days the tweet has been posted for
    retweetScore= reTweets* 0.3333
    #calculates the score for the re-tweets, the 0.3333 is the weight the values recieves
    print("The re-tweet score is:",retweetScore)
    #this prints out the re-tweet score
    replyScore= replies * 0.3333
    #this calculates the reply score, the weight of the score is 33.33 percents, which is why it is multiplied by 0.3333
    print("The reply score is:",replyScore)
    #this prints out the tweet's reply score
    dayScore= (3/numDays) * 0.3333
    #this calculates the day score, which is 3 divided my the number of days a tweet has been posted for, times 0.3333
    print("The day score is:", dayScore)
    #this prints out the day score of the tweet
    totalTweetScore= retweetScore + replyScore + dayScore
    #this will add up the day score, the reply score and the re-tweet score
    print("The tweet's total score is:",totalTweetScore)
    #this gives the user the total tweet score
    #this is the solution to the problem, and it gives the user the tweet's popularity score.
    print("Thank you for using this program, have a nice day!")
    #says goodbye to the user

main()

        
