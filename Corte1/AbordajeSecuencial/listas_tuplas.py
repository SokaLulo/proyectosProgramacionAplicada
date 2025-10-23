#################LISTAS####################
###########################################

# Se crea una lista con varios colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

#input()   
print(my_lista)             # Imprime toda la lista
print(type(my_lista))       # Imprime el tipo de dato (list)
print(my_lista[2])          # Imprime el elemento en la posición 2 ("Amarillo")

print("my_lista size: ", len(my_lista))  # Muestra el tamaño (número de elementos) de la lista
print(my_lista[0:2])        # Imprime desde el índice 0 hasta antes del 2 → ['Rojo', 'Azul']
print(my_lista[:2])         # Igual que arriba, imprime los dos primeros elementos

my_lista.append('Blanco')      # Agrega el elemento "Blanco" al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')    # Inserta "Negro" en la posición 3
print(my_lista)

my_lista.extend(['Marron', 'Gris'])   # Agrega (concatena) varios elementos de otra lista
print(my_lista)

print(my_lista.index('Azul'))   # Devuelve la posición (índice) donde está "Azul"

#my_lista.remove('Magenta')    # Elimina "Magenta" (si existe) → está comentado
my_lista.remove('Marron')      # Elimina el primer elemento con valor "Marron"
print(my_lista)

my_lista.insert(8, 'Marron')   # Inserta "Marron" en la posición 8
print(my_lista)

print(my_lista.pop())          # Elimina y devuelve el último elemento de la lista
size = len(my_lista)           # Obtiene el tamaño de la lista
print("size = ", size)
#print(my_lista.pop(size))     # (Comentado) eliminaría el elemento en la posición "size"

my_lista_3 = my_lista*3        # Repite la lista 3 veces
print("my_lista_3: ", my_lista_3)

print("Sort:")                 # Título
print()
my_listaSort = my_lista.sort() # Ordena la lista alfabéticamente (devuelve None)
print(my_listaSort)            # Imprime None porque sort() modifica en el lugar

# Lista de números desordenados
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()              # Ordena la lista de menor a mayor
print(my_NumList)
#OrderedLList = my_NumList.sort()  # (Comentado) mismo efecto que arriba
#print(my_listaSort)

# Ordenando lista de mayor a menor
my_NumList.sort(reverse = True) # Ordena la lista en orden descendente
print("De menor a mayor: ", my_NumList)  # Imprime la lista ordenada de mayor a menor



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, 
# la diferencia es que son inmutables (no se pueden modificar)

#Convertir una lista a tupla:
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")

my_tupla = tuple(my_lista)     # Convierte la lista "my_lista" en una tupla
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])             # Imprime el primer elemento de la tupla
print(my_tupla[2])             # Imprime el tercer elemento de la tupla

# Evaluar si un elemento está contenido en la tupla (devuelve True o False)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))  # Cuenta cuántas veces aparece "Rojo" en la tupla

# Tupla con un solo elemento (sin coma es solo un string)
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

# Empaquetado de tupla (se puede crear sin paréntesis)
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado de tupla: asigna cada valor a una variable
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

# Imprime los valores desempaquetados en una misma línea
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertir una tupla en una lista
my_lista2 = list(my_tupla)
print(my_lista2)
