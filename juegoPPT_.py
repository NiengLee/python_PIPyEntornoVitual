import random

print('************************************************************\n')
print('Welcome to "rock-paper-scissors" game\n')
print('************************************************************\n')

options = ('rock', 'paper', 'scissors')
decision = True
win = 0
lose = 0
tie = 0

while decision == True:
    print('************************************************************\n')
    user_dec = input('Select rock, paper or scissors : ')
    user_dec = user_dec.lower()
    IA_dec = random.choice(options)

    print('\nYou have choiced : %s \n' % (user_dec))
    print('The system have choiced : %s \n' % (IA_dec))

    while not user_dec in options:
        print('WARNING: you must choose beetween rock, paper, or scissors\n')
        user_dec = input('Select rock, paper or scissors : ')
        user_dec = user_dec.lower()

    if user_dec == IA_dec:
        tie += 1
        print(' --- --- Tie! --- --- ')
    elif user_dec == 'paper' and IA_dec == 'scissors':
        lose +=1
        print(' --- --- You have lost this round! --- --- ')
    elif user_dec == 'rock' and IA_dec == 'paper':
        lose +=1
        print(' --- --- You have lost this round! --- --- ')
    elif user_dec == 'scissors' and IA_dec == 'rock':
        lose +=1
        print(' --- --- You have lost this round! --- --- ')
    elif user_dec == 'paper' and IA_dec == 'rock':
        win +=1
        print(' --- --- You have WON this round! --- --- ')
    elif user_dec == 'rock' and IA_dec == 'scissors':
        win +=1
        print(' --- --- You have WON this round! --- --- ')
    elif user_dec == 'scissors' and IA_dec == 'paper':
        win +=1
        print(' --- --- You have WON this round! --- --- ')


    print('Rounds you have won: %d' % (win))
    print('Rounds you have lost: %d' % (lose))
    print('Rounds tied: %d' % (tie))

    again = input('\nDo you want to play again? (yes/no): ')
    print('\n')
    again = again.lower()

    if again == 'yes':
        decision = True
    elif again == 'no':
        print('Thanks for playing')
        decision = False
    else:
        print('You have answered something different to "yes or no", the game is over')
        print('Thanks for playing')
        decision = False