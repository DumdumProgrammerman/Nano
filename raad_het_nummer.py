def raad_het_nummer():
    import random

    numbers_of_guesses = 3
    random_number = random.randint(1,10)

    print("Welkom bij raad het nummer, wat is je naam?")
    name = input("Voer je naam in: ")

    print(f"Hoi {name}, kan jij de correcte nummer tussen de 1 en 10 raden?")
    print (f'Je hebt {numbers_of_guesses} kansen om het juiste nummer te raden')

    for guesses in range(1, numbers_of_guesses + 1):
        guess = int(input(f'Poging {guesses} van {numbers_of_guesses} - raad het nummer: '))

        if guess == random_number:
            print("Gefeliciteerd, je hebt het nummer geraden!")
            break
        elif guess != random_number:
            print("Jammer, dat is 'm niet")

    if guess != random_number:
        print(f"Sorry {name}, je hebt al je kansen benut. Het juiste nummer was {random_number}")

# raad_het_nummer()