from random import randrange
from icecream import ic

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input('? '))
        except ValueError:
            continue
        if guess == number:
            ic('You win!')
            break
def _main():
    number = randrange(100)
    while True:
        guess = int(input('? '))
        if guess == number:
            ic('You win!')
            break

if __name__  == '__main__':
    main()
