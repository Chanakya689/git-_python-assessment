#Given Input: Target: 42 | User Guess: 50 
#Expected Output: I'm thinking of a number between 1 and 100.
#  (10 left) Enter guess: 45 Higher! 
# (9 left) Enter guess: 97 Lower! 
# (8 left) Enter guess: 52 Higher!
#  (7 left) Enter guess: 85 Lower! 
# (6 left) Enter guess: 93 Lower! 
# (5 left) Enter guess: 54 Correct! 
# The number was 54.

from random import randint

target = randint(1, 100)
print(f"I'm thinking of a number between 1 and 100.")

guesses_left = 10
while guesses_left > 0:
    guess = int(input(f"({guesses_left} left) Enter guess: "))
    if guess < target:
        print("Higher!")
    elif guess > target:
        print("Lower!")
    else:
        print(f"Correct! The number was {target}.")
        break
    guesses_left -= 1

