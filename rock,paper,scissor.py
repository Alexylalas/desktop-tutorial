#since we want a user to input the data
#we need random for the computer
import random

def play():
    user=input("whats your choice [R] for rock, [P]  for paper,[S] for scissor")
    c=random.choice(['r','p','s'])

    if user == c:
        print(" we have a tie")

    if is_win(user, c):
        print("you win")

    print("you lose")

def is_win(player, opponent):
    #r > s , s > p , p > r
    (player =='r' and opponent=='s') or (player=='s' and opponent=='p')\
    (player=='p' and opponent =='r')
    return True;