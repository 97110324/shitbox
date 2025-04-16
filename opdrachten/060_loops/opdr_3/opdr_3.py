# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []


for i in range(3, 82, 3):  # Begin bij 3, eindig bij (en inclusief) 81, tel telkens 3 op
    berekening = (i ** 2) / 3  # Bereken het kwadraat van i en deel het door 3
    my_list.append(berekening)  # Voeg het resultaat toe aan de lijst

# Print de resulterende lijst
print(my_list)