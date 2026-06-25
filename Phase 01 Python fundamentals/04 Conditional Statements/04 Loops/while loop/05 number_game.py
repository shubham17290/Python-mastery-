"""import random

com = random.randint(1, 100)
tries = 0
while True:
    tries = tries + 1

    hum = int(input("Guess your number between 1 to 100 :- "))
    if hum == com:
        print(f"congratulation you have won in {tries} tries !")
        break

    elif hum > com:
        print(" sorry wrong guess go lower !, please go little higher ")

    elif hum < com:
        print("sorry you guess higher number !, please go little lower ")
"""

import random

secret_number = random.randint(1, 100)
tries = 0
while True:
    tries = tries + 1

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("You Won!")
        
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")
