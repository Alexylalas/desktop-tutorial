
#python project Guessing the number 

#importing the necessary library

import random
import math

#input of the upper and the lower values
upper=int(input("enter the upper values"))
lower=int(input("enter the lower values"))

# selecting a random number between the range
x= random.randint(lower,upper)


#the number of chances for guessing 
print("you have ",round(math.log(upper - lower + 1,2)),"chances")
#assigning a variable
count=0


while count< math.log(upper-lower+1,2):
    count+=1

    guess=int(input("Guess a value"))

    if guess == x:
        print("congratulations you did it!!!")
    
    elif x > guess:
        print("too Low")
    
    elif x < guess:
        print("too high")
 
count>=math.log(upper -lower+1,2)
print("Sorry you are out of chances ")
print(" The value was",x)