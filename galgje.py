import random

def random_woord_picker():
    with open("woordenlijst.txt", "r") as file:
        woordenlijst = file.read().split()
    return random.choice(woordenlijst).lower()

def woord_display(woord, correcte_gok):
    return ''.join([letter if letter in correcte_gok else '_' for letter in woord])

def galgje():
    woord = random_woord_picker()
    correcte_gok = []
    verkeerde_gok = []
    aantal_pogingen = 10
    aantal_pogingen_counter = 0
    print("Dit is Galgje!\nJe hebt 12 pogingen.\nRaad het woord!")

    while aantal_pogingen_counter < aantal_pogingen:
        print(f"\nWoord: {woord_display(woord, correcte_gok)}")
        print(f"Verkeerde letters: {', '.join(verkeerde_gok)}")
        print(f"Resterende pogingen: {aantal_pogingen - (aantal_pogingen_counter)}")
        gok = input("Raad een letter: ")

        if gok in correcte_gok or gok.lower() in verkeerde_gok:
            print(f"Je hebt de letter '{gok}' al gebruikt.")

        elif gok in woord:
            correcte_gok.append(gok)
            print(f"De letter '{gok.upper()}' zit in het woord!")

        else:
            verkeerde_gok.append(gok)
            aantal_pogingen_counter += 1
            print(f"Helaas, de letter '{gok.upper()}' zit niet in het woord.")

        if all(letter in correcte_gok for letter in woord):
            print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden!")
            break

        if aantal_pogingen_counter == aantal_pogingen:
            print(f"\nhet juiste woord was '{woord}', probeer het nog eens")
galgje()
