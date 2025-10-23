# Diccionario con edificios y sus alturas 
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, 
                    "Abraj Al Bait": 601, "Ping An": 599, 
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Acceder a valores usando las claves
print(building_heights["Burj Khalifa"])  # Muestra 828
print(building_heights["Ping An"])       # Muestra 599


# Diccionario que agrupa signos del zodiaco por elemento
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
                   "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"],
                   "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])  # Lista de signos de tierra
print(zodiac_elements["fire"])   # Lista de signos de fuego


# Acceder a una clave inexistente genera un error KeyError
# print(building_heights["Landmark 81"])  # Descomentar para probar


# Comprobar si una clave existe antes de acceder a ella
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])  # Solo se ejecuta si la clave existe


# Agregar un nuevo par clave-valor al diccionario
zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Muestra el valor recién agregado


# Uso del método .get() para acceder a valores de forma segura
print(building_heights.get("Shanghai Tower"))  # Devuelve 632
print(building_heights.get("My House"))        # Devuelve None (no genera error)


# Diccionario con identificadores de usuario
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 102931, 
            "keysmithKeith": 129384}

# Obtener valores con .get()
print(user_ids.get("teraCoder"))  # Devuelve 100019

# Usar condicionales para asignar un valor por defecto si la clave no existe
if user_ids.get("teraCoder") is None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")
print(tc_id)  # Muestra 100019

if user_ids.get("superStackSmash") is None:
    stack_id = 100000
print(stack_id)  # Muestra 100000 (valor asignado por defecto)


# Eliminar elementos usando .pop()
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 
          320291: "Gift Basket", 412123: "Necklace", 
          298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))  # Elimina y devuelve "Gift Basket"
print(raffle)

print(raffle.pop(100000, "No Prize"))  # Clave inexistente → devuelve "No Prize"
print(raffle)

print(raffle.pop(872921, "No Prize"))  # Elimina y devuelve "Concert Tickets"
print(raffle)


# Ejemplo tipo juego: objetos disponibles y puntos de salud
available_items = {"health potion": 10, "cake of the cure": 5, 
                   "green elixir": 20, "strength sandwich": 25, 
                   "stamina grains": 15, "power stew": 30}
health_points = 20

# Sumar puntos de salud y eliminar los objetos usados
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)  # No existe, devuelve 0

print(available_items)   # Objetos restantes tras usar algunos
print(health_points)     # Salud total después de sumar


# Obtener todas las claves de un diccionario
test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81], 
               "Sylvia": [80, 82, 84], "Pedro": [98, 96, 95], 
               "Martin": [78, 80, 78], "Dina": [64, 60, 75]}

print(list(test_scores))  # Convierte las claves en una lista
for student in test_scores.keys():
    print(student)        # Imprime cada nombre de estudiante


# Obtener las claves de varios diccionarios distintos
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 102931, 
            "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, 
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


# Obtener todos los valores de un diccionario
for score_list in test_scores.values():
    print(score_list)  # Muestra las listas de notas de cada estudiante

# Calcular la suma total de ejercicios de programación
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, 
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # Muestra la suma total de ejercicios


# Recorrer todos los pares clave-valor usando .items()
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, 
                  "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


# Ejemplo final: porcentaje de mujeres en distintas profesiones
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, 
                           "Pharmacist": 58, "Physician": 40, 
                           "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
