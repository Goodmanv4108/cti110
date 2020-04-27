#This coding is a random number guessing generator.
#4/26/2020
#CTI-110 P5HW1 - Random Number
#Veronica Goodman
#


import random

guess = 0

def main():
    print('MAIN MENU')
    print('---------')
    print('1) Play Game')
    print('2) Exit')
    game=int(input())
    if game == 1:
        random_number()

def random_number():
    x = random.randint(1,100) 
    print('I am thinking of a number between 1 to 100. Can you guess it?')
    play_game(x)

def play_game(x):
    num = int(input())
    global guess
    guess += 1
    if num == x:
        print('Congrats! You got it!')
        print('It only took you',guess,'tries!')
        print('')
        guess = 0
        main()

    elif num >= x:
        print('Too high, try again.')
        play_game(x)
    elif num <= x:
        print('Too low, try again.')
        play_game(x)


main()
