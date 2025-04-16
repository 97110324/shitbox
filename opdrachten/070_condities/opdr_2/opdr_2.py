# Opdracht 2 condities
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = [43948, 878768, 38768, 87555, 765765]

# Maak een lege lijst om de resultaten op te slaan
deelbaar_door_3 = []

# Loop door elk getal in de lijst
for getal in my_list:
    if getal % 3 == 0:  # Controleer of het getal deelbaar is door 3
        deelbaar_door_3.append(getal)  # Voeg het getal toe aan de nieuwe lijst

# Print de resulterende lijst
print(deelbaar_door_3)

# for...:
#   if...:
#       print()