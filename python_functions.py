# importing random library to use to generate random numbers
import random as rd

def coin_flips(num_trials):
    heads = 0
    tails = 0 
    randominput=0
    head_limit = 0.5

    #using for loop to generate 100 random numbers between [0,1] with the help of random function
    for i in range(num_trials):
        randominput=rd.random()

        # using if state to set the condition for deciding where in  between 
        # 0 to 1 head lies i.e 0-0.5 or 0.5 to 1
        if randominput>=0.5:
            #if random number genreated is between 0.5 and 1 then it will increase head count by 1
            heads +=1
        else:
            #if random number genreated is not between 0.5 and 1 then it will increase tails count by 1
            tails +=1

    print("number of heads ", heads)
    print("Percentage of heads ", (heads/num_trials)*100,"%")
    print("number of tails ", tails)
    print("Percentage of heads ",(100-((heads/num_trials)*100)),"%")

# calling coin_flips function
coin_flips(200)
coin_flips(2000)
coin_flips(1000)