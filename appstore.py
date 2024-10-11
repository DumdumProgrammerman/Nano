import galgje
import raad_het_nummer

print("Welkom bij de Nuna Appstore\nKies uit een van de volgende games:\n\tDruk 1 voor Galgje.\n\tDruk 2 voor Raad het nummer. ")
keuze = input("Welk spel wil je spelen?: \n")

if keuze == "1":
    galgje.galgje()

if keuze == "2":
    raad_het_nummer.raad_het_nummer()