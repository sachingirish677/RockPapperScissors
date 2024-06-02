# RockPapperScissors

This is a simple implementation of the classic Rock, Paper, Scissors game in Python. The game is played between a user and the computer.

# How the Game Works

1.The user is prompted to enter their choice of 'r' for rock, 'p' for paper, or '' for scissors.
2.The computer's choice is generated randomly using the random.choice function.
3.The game then determines the winner based on the game's rules:
    a.Rock beats Scissors (because rock can crush scissors)
    b.Scissors beats Paper (because scissors can cut paper)
    c.Paper beats Rock (because paper can cover rock)
    d.If both the user and the computer choose the same option, it's a tie.
4.The game then prints out the result, indicating whether the user won, lost, or tied.
