# Opdracht 1 functies
# Naam student:
# Groep:

def volledige_naam(lijst_met_namen):
    """
    Combineert de voornaam, tussenvoegsel en achternaam tot een volledige naam.

    :param lijst_met_namen: Lijst met dictionaries die voornaam, tussenvoegsel en achternaam bevatten
    :return: Geen return-waarde; print de volledige namen
    """
    for persoon in lijst_met_namen:
        # Haal de waarden uit de dictionary
        voornaam = persoon.get("voornaam", "")
        tussenvoegsel = persoon.get("tussenvoegsel", "").strip()  # Verwijder eventuele spaties
        achternaam = persoon.get("achternaam", "")

        # Combineer de namen, zorg dat er geen dubbele spaties zijn
        if tussenvoegsel:
            volledige = f"{voornaam} {tussenvoegsel} {achternaam}"
        else:
            volledige = f"{voornaam} {achternaam}"

        # Print de volledige naam
        print(volledige.strip())


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)