# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

# Maak een lijst met vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]


def vraag_feestganger():
    """Bevraag een feestganger en retourneer de antwoorden als dictionary."""
    antwoorden = {}
    for index, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{index}. {vraag} ")
        # Sla het antwoord op in de dictionary
        if "voornaam" in vraag:
            antwoorden["voornaam"] = antwoord
        elif "achternaam" in vraag:
            antwoorden["achternaam"] = antwoord
        elif "drank" in vraag:
            antwoorden["drank"] = antwoord
        elif "eten" in vraag:
            antwoorden["eten"] = antwoord
    return antwoorden


def schrijf_naar_bestand(gegevens):
    """Schrijf de gegevens van een feestganger naar een tekstbestand."""
    with open("feestgangers.txt", "a") as bestand:  # Open het bestand in append-modus
        bestand.write("----\n")
        for key, value in gegevens.items():
            bestand.write(f"{key}: {value}\n")
        bestand.write("----\n")


# Hoofdprogramma
print("Welkom bij het Amerikaanse party-organisatieformulier!")
while True:
    # Vraag of de gebruiker wil doorgaan
    doorgaan = input("Wil je een feestganger toevoegen? (ja/nee): ").lower()
    if doorgaan != "ja":
        break

    # Bevraag de feestganger
    antwoorden = vraag_feestganger()

    # Schrijf de antwoorden naar het tekstbestand
    schrijf_naar_bestand(antwoorden)

    # Geef feedback
    print("Bedankt voor het invullen! See you at the party.\n")

print("Alle gegevens zijn opgeslagen in 'feestgangers.txt'.")

# Party enquete