# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

print("Welkom bij 'Raad een nummertje'!")
print("Probeer te raden welk getal ik heb uitgekozen (tussen 1 en 100).")

while True:
    invoer = input("Raad mijn geheime getal: ")

    if not invoer.isdigit():
        print("Ongeldige invoer! Voer een getal in.")
        continue

    geraden_getal = int(invoer)
    aantal_pogingen += 1

    if geraden_getal < geheim_getal:
        print("Hoger!")
    elif geraden_getal > geheim_getal:
        print("Lager!")
    else:
        print(f"Je hebt het getal geraden! Het was {geheim_getal}.")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan.")
        break

with open("raadspel_resultaten.txt", "w") as bestand:
    bestand.write(f"Te raden getal: {geheim_getal}\n")
    bestand.write(f"Aantal pogingen: {aantal_pogingen}\n")

print("De resultaten zijn opgeslagen in 'raadspel_resultaten.txt'.")

