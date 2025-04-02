# Opdracht 1 lists
# Naam student: [ Jouw naam ]
# Groep: [ Jouw groep ]

# Maak een lege list
mylist = []

# Maak 4 dictionaries voor personen
dict_1 = { "id": 0, "voornaam": "Jan", "achternaam": "Jansen" }
dict_2 = { "id": 1, "voornaam": "Piet", "achternaam": "Pietersen" }
dict_3 = { "id": 2, "voornaam": "Klaas", "achternaam": "Klaassen" }
dict_4 = { "id": 3, "voornaam": "Cor", "achternaam": "Corsi" }

# Voeg de dictionaries toe aan de list met de append-methode
mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

# Print de volledige naam van de 2e persoon
print(mylist[1]["voornaam"], mylist[1]["achternaam"])