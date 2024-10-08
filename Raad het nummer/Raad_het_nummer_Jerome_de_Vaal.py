import random

numbers_of_guesses = 3
random_number = random.randint(1,10)

print("Hello, what's your name?")
name = input("Please provide your name: ")

print(f"Hello {name}, can you guess the correct number between 1 and 10?")
print (f'You have {numbers_of_guesses} chances to guess the correct number')

for guesses in range(1, numbers_of_guesses + 1):
    guess = int(input(f'Attempt {guesses}: Guess the number: '))

    if guess == random_number:
        print("Congratulations, you guessed the number!")
        break
    elif guess != random_number:
        print("Unfortunate")

if guess != random_number:
    print(f"Sorry {name}, you've used all your attempts. The correct number was {random_number}")

