import random

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock,paper, or scissors?: ').lower()

    if player == computer:
        print('computer: ',computer)
        print('user: ',player)
        print('its a tie!')

    elif player == 'rock':
        if computer == 'paper':
            print('computer: ',computer)
            print('user: ',player)
            print('paper cover rock, you lose!')
        if computer == 'scissors':
            print('computer: ',computer)
            print('user: ',player)
            print('rock smashes scissors, you win!')

    elif player == 'scissors':
        if computer == 'rock':
            print('computer: ',computer)
            print('user: ',player)
            print('rock smashes scissors, you lose!')
        if computer == 'paper':
            print('computer: ',computer)
            print('user: ',player)
            print('scissors cuts paper, you win!') 

    elif player == 'paper':
        if computer == 'scissors':
            print('computer: ',computer)
            print('user: ',player)
            print('scissors cuts paper, you lose!')
        if computer == 'rock':
            print('computer: ',computer)
            print('user: ',player)
            print('paper cover rock, you win!'):

        play_again = input('play again? (yes/no): ').lower()

        if play_again != 'yes':
             break
print('Good game, Bye!')  