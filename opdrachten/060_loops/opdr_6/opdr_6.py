# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop



pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizzas.sort()
print("Gesorteerde lijst:", pizzas)

pizzas.append('yo-favorito')
print("Lijst met nieuwe pizza:", pizzas)

pizzas.remove('olivio')
print("Lijst na verwijderen van minst favoriete pizza:", pizzas)

eerste_drie = pizzas[:3]
print("Eerste 3 pizza's:", eerste_drie)

middelste_pizza = pizzas[len(pizzas) // 2]
print("Middelste pizza:", [middelste_pizza])

laatste_drie = pizzas[-3:]
print("Laatste 3 pizza's:", laatste_drie)
