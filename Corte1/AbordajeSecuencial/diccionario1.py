# Diccionario que almacena la temperatura (°C) medida por sensores en distintas habitaciones
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Diccionario que indica cuántas cámaras hay instaladas en cada zona
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Mostrar las temperaturas registradas por los sensores
print(sensors)

# Mostrar el número de cámaras por zona
print(num_cameras)

# Diccionario que traduce palabras del inglés a un idioma ficticio (élfico)
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)

## Ejemplo de error: las listas no pueden ser claves en un diccionario (no son inmutables)
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# print(powers)  # Esto generaría: TypeError: unhashable type: 'list'

# Diccionario donde cada familia tiene una lista con los nombres de sus hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
            "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# Crear y mostrar un diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# Diccionario con platos de un menú y sus precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Agregar un nuevo plato al menú
menu["cheesecake"] = 8
print("After", menu)

# Ejemplo de redefinición de un diccionario (el anterior se sobrescribe completamente)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}  # redefinido (sin cambios)
animals_in_zoo = {"horses": 2}     # redefinido (ahora contiene caballos)
print(animals_in_zoo)

## Agregar múltiples pares clave-valor de una sola vez con update()
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# Añadir nuevas habitaciones con sus temperaturas
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

# Diccionario de usuarios con sus respectivos IDs
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

# Añadir nuevos usuarios al diccionario
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

## Sobrescribir valores existentes en un diccionario
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Cambiar el precio de 'oatmeal' (antes 3 → ahora 5)
menu["oatmeal"] = 5
print("After", menu)

# Diccionario con ganadores de los premios Oscar
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()

# Agregar una nueva categoría con su ganadora
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()

# Reemplazar el valor de una categoría existente
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)

### Comprensiones de diccionarios (Dict Comprehensions) ###
# Dos listas con nombres y alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() combina ambas listas en pares (nombre, altura)
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)  # es un objeto iterable (no una lista visible directamente)

# Crear un diccionario usando comprensión: {clave: valor for ...}
students = {key: value for key, value in zip(names, heights)}
# Resultado: {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)

# Listas de bebidas y su contenido de cafeína (mg)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Unir ambas listas con zip()
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)  # objeto zip

# Crear un diccionario {bebida: cafeína}
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# Listas de canciones y su número de reproducciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Crear diccionario con zip()
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)

# Agregar una nueva canción con su número de reproducciones
plays.update({"Purple Haze": 1})

# Actualizar el valor de una canción existente
plays.update({"Respect": 94})
print("After: ", plays)

# Diccionario que contiene otros diccionarios (diccionarios anidados)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
