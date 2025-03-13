from random import randint
from time import sleep

lower_number,higher_number = 1,10
random_number: int = randint(lower_number,higher_number)
print(f'Guess the number from {lower_number} to {higher_number}')

attempts =0
while True:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("Give the valid value")
        continue
    
    attempts += 1
    
    if user_guess > random_number:
        print("the guess is higher number")
    elif user_guess < random_number:
        print("the guess is lower number")
    else:
        print("Yeah!,You got the Number")
        break
    
    if attempts == 3:
        print("Wait for 4 second")
        sleep(4)