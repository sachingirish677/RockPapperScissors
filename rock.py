import random

def play():
    user=input(" Enter your choice \n'r' for rock,'p' for paper,'s' for scissors\n")
    computer=random.choice(['r','p','s'])
    
    if user==computer:
        return "Its a tie"
    
    if is_win(user,computer):
        return 'You Won'
    
    if is_win(computer,user):
        return 'You Lost'
    
def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    
print(play())