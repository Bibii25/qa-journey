import random

secret = random.randint(1, 20)
guess_count = 0
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    guess_count += 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break
    if guess_count == 5:
            print(f"Out of guesses! The number was... {secret}")
            break
if guess == secret:
    print(f"You guessed the number in  {guess_count} attempts")
