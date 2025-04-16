# Opdracht 3 condities
# Naam student:
# Groep:



normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijdsgroepen = {
    "baby": (0, 2),
    "kinderen": (3, 18),
    "volwassenen": (19, 64),
    "ouderen": (65, 150),
}

leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

groep = None
for categorie, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        groep = categorie
        break

if groep is None:
    print("Ongeldige leeftijd!")
else:

    korting_percentage = kortings_percentages[groep]
    korting_bedrag = normale_toegangsprijs * (korting_percentage / 100)
    te_betalen_prijs = normale_toegangsprijs - korting_bedrag

    print(f"U behoort tot de groep {groep}")
    print(f"U krijgt {korting_percentage}% korting")
    print(f"U betaalt daarom {te_betalen_prijs:.2f}")

# Hier komt je code...
