# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

gevonden = False
for topping, prijs in toppings:
    if keuze == topping:
        print(f"U heeft {topping} besteld. Dat kost {prijs:.1f}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")

# Hier de rest van jouw code...