# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math

# Functie om de schuine zijde te berekenen met de stelling van Pythagoras
def bereken_schuine_zijde(zijde1, zijde2):
    # De stelling van Pythagoras: c = √(a² + b²)
    schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)
    return schuine_zijde

# Hoofdprogramma
def main():
    print("Geef de lengte van de eerste zijde")
    zijde1 = float(input("> "))  # Invoer van de eerste zijde als float

    print("Geef de lengte van de tweede zijde")
    zijde2 = float(input("> "))  # Invoer van de tweede zijde als float

    # Bereken de schuine zijde
    schuine_zijde = bereken_schuine_zijde(zijde1, zijde2)

    # Print het resultaat
    print(f"\nDe lengte van de schuine zijde is: {schuine_zijde:.7f}")

# Voer het hoofdprogramma uit
if __name__ == "__main__":
    main()