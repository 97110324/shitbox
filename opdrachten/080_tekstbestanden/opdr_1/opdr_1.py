# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Stel de vragen
vraag_1 = input("Wat vind je van de huidige regering?\n")
vraag_2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag_3 = input("Wat vind jij de mooiste stad van Nederland?\n")

# Open een tekstbestand om de antwoorden op te slaan
with open("enqueteresultaten.txt", "w") as bestand:
    # Schrijf de vragen en antwoorden naar het bestand
    bestand.write("Enquete Resultaten:\n")
    bestand.write(f"Wat vind je van de huidige regering? {vraag_1}\n")
    bestand.write(f"Wat vind je van de Python-lessen tot nu toe? {vraag_2}\n")
    bestand.write(f"Wat vind jij de mooiste stad van Nederland? {vraag_3}\n")

print("Bedankt voor je deelname! De resultaten zijn opgeslagen in 'enqueteresultaten.txt'.")