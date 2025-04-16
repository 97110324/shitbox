# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

invoer = input("Voer minimaal 5 objecten in, gescheiden door komma's: ")


objecten = [item.strip() for item in invoer.split(",")]


if len(objecten) < 5:
    print("Je moet minimaal 5 objecten invoeren!")
else:

    objecten.sort(reverse=True)


print(objecten)