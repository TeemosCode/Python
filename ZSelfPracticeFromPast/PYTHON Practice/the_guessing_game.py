#the guessing game

import random
def game():
    count = 0
    number = random.randint(0,99)
    while True:
        guess = int(input("Guess a number(int) :"))
        count += 1
        print(number)
        if guess == number:
            print("Congratulations!!!!You got it right yo!")
            break
        elif count == 10:
            print("You missed your chance boy")
            break
        elif guess > number:
            print("your guess is too big boy~~~")
            print("Times you guessed:%d　; Chances left:%d"%(count, 10-count))
        elif guess < number:
            print("your guess is too small boy~~~")
            print("Times you guessed:%d　; Chances left:%d"%(count, 10-count))



game()
