
# Nuna Appstore

Welkom bij de **Nuna Appstore**! In deze terminal-app kun je kiezen uit twee klassieke spellen: **Galgje** en **Raad het Nummer**.

## Inhoud

1. [Beschrijving](#beschrijving)
2. [Installatie](#installatie)
3. [Gebruik](#gebruik)
4. [Bestanden](#bestanden)
5. [Voorbeeldoutput](#voorbeeldoutput)
6. [Bijdragen](#bijdragen)
7. [Licentie](#licentie)

## Beschrijving

Dit is een school project van de Hogeschool Utrecht voor Project Nano van Jerôme de Vaal

De Nuna Appstore biedt de keuze uit twee spellen:

1. **Galgje**: Raad het verborgen woord door letters te raden. Je hebt 10 pogingen om het woord te raden.
2. **Raad het Nummer**: Raad het juiste nummer tussen 1 en 10 binnen 3 pogingen.

## Installatie

1. **Clone of download de repository**:
   ```bash
   git clone https://github.com/dumdumprogrammerman/nano.git
   ```

2. **Installeer Python** (vereist Python 3.6+). Je kunt Python [hier](https://www.python.org/downloads/) downloaden.

3. **Voer het hoofdscript uit**:
   ```bash
   python appstore.py
   ```

## Gebruik

1. Open een terminal en navigeer naar de directory van de Nuna Appstore.
2. Start het programma met het volgende commando:
   ```bash
   python appstore.py
   ```
3. Kies welk spel je wilt spelen door een keuze te maken uit de beschikbare opties.

### Spelopties:

- **Druk 1 voor Galgje**: Het spel kiest willekeurig een woord, en je probeert dit woord te raden door letters in te voeren.
- **Druk 2 voor Raad het Nummer**: Het spel kiest een willekeurig nummer tussen 1 en 10, en je moet het juiste nummer binnen 3 pogingen raden.

## Bestanden

- **appstore.py**: Het hoofdscript dat de spellen samenbrengt.
- **galgje.py**: Script voor het Galgje-spel.
- **raad_het_nummer.py**: Script voor het Raad het Nummer-spel.
- **woordenlijst.txt**: Woordenlijst voor het Galgje-spel.

## Voorbeeldoutput

### Galgje:
```
Welkom bij Galgje!
Je hebt 10 pogingen.
Raad het woord!

Woord: _ _ _ _
Verkeerde letters: 
Resterende pogingen: 10
Raad een letter: a
De letter 'A' zit in het woord!
```

### Raad het Nummer:
```
Welkom bij Raad het Nummer, wat is je naam?
Voer je naam in: Jerome
Hoi Jerome, kan jij de correcte nummer tussen de 1 en 10 raden?
Je hebt 3 kansen om het juiste nummer te raden.
Poging 1 van 3 - raad het nummer: 5
Jammer, dat is 'm niet.
```

