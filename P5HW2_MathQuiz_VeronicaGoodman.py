#This program gives the user a simple math quiz for the user to answer.
#4/29/2020
#CTI-110 P5HW2 - Math Quiz
#Veronica Goodman
#


import random

def main():
    print('MAIN MENU')
    print('---------')
    print('1) Add Random Numbers')
    print('2) Subtract Random Numbers')
    print('3) Exit')
    quiz=int(input())
    if quiz == 1:
        add_numbers()

    elif quiz == 2:
        subtract_numbers()

def add_numbers():
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    correct = x + y
    print(' ', x)
    print('+', y)
    answer = int(input())
    if correct == answer:
        print('Awesome, you got it right!')
        print('')
        main()
    else:
        print('Incorrect. The correct answer is',correct)
        print('')
        main()

def subtract_numbers():
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    correct = x - y
    print(' ', x)
    print('-', y)
    answer = int(input())
    if correct == answer:
        print('Awesome, you got it right!')
        print('')
        main()
    else:
        print('Incorrect. The correct answer is',correct)
        print('')
        main()

main()
