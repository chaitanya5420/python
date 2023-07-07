
# ------------------------------------------------------------------------200 - 300 --------------------------------------------------------------------------

# 1- In Chefland, everyone who earns strictly more than Y rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.
# You have earned (X>Y) rupees this year. Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.

# T = int(input())
# for i in range(T):
#     (x,y) = map(int,input().split(' '))
    
#     if x>y:
#         diff = x-y
#         print(diff)
        


# 2- Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day.Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not        
# T = int(input())

# for i in range(T):
#     water_intake = int(input())
#     if water_intake>2000:
#         print("YES")
#     else:
#         print("NO")




# 3- Chef has been working hard to compete in MasterChef.He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.
# Check whether Chef made it to the top 10 or not?
# T =int(input())

# for i in range(T):
#     chef_ranking= int(input())
#     if chef_ranking <= 10:
#         print("YES")
#     else:
#         print("NO")
        
        
        
        
# 4 - Chef's son wants to go on a roller coaster ride. The height of Chef's son is X inches
# while the minimum height required to go on the ride is H inches. Determine whether he can go on the ride or not.
# Roller Coaster
# T = int(input())

# for i in range(T):
#     x,h = map(int , input().split(' '))
    
#     if x >=h :
#         print("YES")
#     else:
#         print("NO")




#5 - Chef had collected N notes of Rs.2000 to pay his total college fees. However, the government banned Rs. 2000 notes.Chef wants 
# to pay the same amount using Rs. 500notes only. Find the number of notes Chef needs
# 2000

# total_notes = int(input())
# notes_need = (total_notes*2000)//500
# print(notes_need)



# 6- You need to output the number of new users in the contest who, after the contest, will get a rating and also the number of new users who will get a rating strictly greater than 1000
# Each input file contains of a single line, with three integers N,A and B - the number of new users, the number of users who just saw the problem and didn't make any submission, and the number of users who made a submission but could not solve any problem correctly.
# My very 1st contest!

# (n,a,b) = map(int , input().split(' '))

# get_rating    = n-a
# higher_than_1000 = get_rating - b

# print(get_rating  , higher_than_1000)



# 7- Currently there are courses for 4 languages, and hence there are 8 courses in this section. But suppose there are courses for N languages, what will be the total number of courses in this section?
# CodeChef Learn Problem Solving
# n = int(input())

# total_courses = n*2
# print(total_courses)



# -----------------------------------------------------------------start rating 300-400---------------------------------------------------------------------------------------------------------


# 1- Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
# Second Max of Three Numbers
# N = int(input())

# for i in range(N):
#     lst = list(map(int , input().split(' ')))
#     lst.sort()
#     print(lst[1])



#2-  In a certain month, Chef earned X rupees while Chefina earned Y rupees such that y>X.Since they want to end up with exactly the same amount, they decide to donate the difference between their income to a charity.Find the amount they donate in the month.
# Chef and Donation

# T =int(input())

# for i in range(T):
#     x,y = map(int , input().split())
    
#     donating = y-x
#     print(donating)



# 3- Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.The meeting platform supports a meeting of maximum 3030 minutes without subscription and a meeting of unlimited duration with subscription.Determine whether Chef needs to take a subscription or not for setting up the meet.
# Get Subscription

# T =int(input())

# for i in range(T):
#     x= int(input())
    
#     if x > 30 :
#         print("YES")
#     else:
#         print("NO")


#4- Chef has recently started playing chess, and wants to play as many games as possible.he calculated that playing one game of chess takes at least 2020 minutes of his time.Chef has N hours of free time. What is the maximum number of complete chess games he can play in that time?
# Chess Time

# T =int(input())

# for i in range(T):
#     x= int(input())
    
#     highest_hour = 60*(x)//20
#     print(highest_hour)


# 5- Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.Given that Chef bought the stock at value X and sold it at value y. Help him calculate whether he made a profit, loss, or was it a neutral deal.
# Bull or Bear

# T =int(input())
 
# for i in range(T):
#     x,y = map(int , input().split())
     
#     if  x > y:
#          print("LOSS")
#     elif y > x:
#         print("PROFIT")
#     else:
#         print("NEUTRAL")




# 6- Alice, Bob and Charlie are bidding for an artifact at an auction.Alice bids A rupees, Bob bids B rupees, and Charlie bids C rupees (where A, B, and C are distinct).According to the rules of the auction, the person who bids the highest amount will win the auction.Determine who will win the auction.
# Bidding

# T = int(input())

# for i in range(T):
    
#     a,b,c = map(int , input().split())
    
#     result = {a:'Alice' , b:'Bob' , c:'Charlie'}
#     print(result[max(result)])



# -----------------------------------------------------------------400-500---------------------------------------------------------------------------------------
# -----------------------------------------------------------------500-600---------------------------------------------------------------------------------------