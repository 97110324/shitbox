# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...


gasten = []

# Voeg de gasten toe aan de lijst
gasten.append("Jij")
gasten.append("Paul")
gasten.append("Kees")
gasten.append("Marie")
gasten.append("Hilda")

# Print de lijst met alle gasten
print("Lijst met gasten na het toevoegen:")
print(gasten)

# Marie belt dat ze niet meer meegaat, haal haar uit de lijst
gasten.remove("Marie")

# Print de lijst zonder Marie
print("\nLijst met gasten nadat Marie afzegt:")
print(gasten)

# George wil ook mee en wil naast Kees zitten
# Vind de index van Kees in de lijst
kees_index = gasten.index("Kees")

# Voeg George toe naast Kees (index + 1)
gasten.insert(kees_index + 1, "George")

# Print de uiteindelijke lijst met gasten
print("\nUiteindelijke lijst met gasten:")
print(gasten)