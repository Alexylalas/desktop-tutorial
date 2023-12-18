#since we want a user to input the data
#we need random for the computer

import random

def play():
    user=input("whats your choice 's' for rock, 'p'  for paper , 's' for scissor\n")
    c=random.choice(['r','p','s'])

    if user == c:
        return(" we have a tie")

    if is_win(user, c):
        return "you win"

    return "you lose"

def is_win(player, opponent):
    #r > s , s > p , p > r
    if(player =='r' and opponent=='s') or (player=='s' and opponent=='p') or\
        (player=='p' and opponent =='r'):
        return True
    
print(play())