""""er wordt 3 maal bijgehouden welke letters er worden gebruikt.
- Voor het woord,
- voor galgje zelf en
- welke niet in het woord zitten.

aftellen in pogingen"""


import random

def random_woord_picker():
    with open("woordenlijst.txt","r") as file:
        woordenlijst = file.read().split()
    return random.choice(woordenlijst)

random_woord = random_woord_picker()
aantal_pogingen = 10

def user_input():
    geraden_letter = str(input("Geef een letter: "))

    print(f"je hebt nog {aantal_pogingen}")
    aantal_pogingen - 1
# print(random_woord_picker())

