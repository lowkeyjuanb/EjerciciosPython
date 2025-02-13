# # Listas 

# Las listas permiten guardar MULTIPLES variables DENTRO de UNA variable.

# Las variables dentro de una lista pueden estar duplicadas

# Ejemplo de una lista de spirits [tipo STRING]
listaAlcohol = ["Tequila", "Vodka", "Whisky", "Tequila", "Vodka"]

# Ejemplo de una lista de valores NUMERICOS [float, int]

listaNumeros = [10, 2.1, 48]

# Ejemplo de una lista de valores bool (booleanos)

listaBool = [True, False, False] 

# Ejemplo de una lista de valores mixtos.

listaMixta = ["Tequila", 10, True, 50.2]


# Display del tipo de dato que son estas variables

print("Tipo de dato de x lista", type(listaAlcohol))


# Constructor de una lista

ejemploConstructorLista = list(("apple", "pear", "pineapple"))

print("Ejemplo de lista con constructor", ejemploConstructorLista)


# Accesar a un elemento dentro de esta lista
listaAlcohol = ["Tequila", "Vodka", "Ron"]

print("Accesa a n elemento dentro de una lista:", listaAlcohol[0])

print("Accesa al ULTIMO elemento de una lista:", listaAlcohol[-1])

print("Accesa a un rango de elementos dentro de una lista:", listaAlcohol[0:2])

print("Imprime los elementos desde el primero hasta n dato:", listaAlcohol[2:])

# # Ejemplo con condicionales:

if ("Tequila" and "FourLoko") or "Vodka" in listaAlcohol:
    print("Si esta el elemento Tequila y FourLoko o puro vodka en listaAlcohol")
elif "Ron" in listaAlcohol:
    print("Si esta el elemento Ron en listaAlcohol")
else:
    print("No existe el elemento en la lista")


print("---------------------------------------\n")
print("Ejercios")

# METODOS DE LAS LISTAS
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# # Ejercicio 3.1 - Agrega un elemento al final de una lista.
print("\nEjercicio 3.1\n")
listaFrutas = ["Manzana", "Pera", "Platano"]
print(listaFrutas)
listaFrutas.append("Kiwi")
print("Ejercicio 3.1: ", listaFrutas)

# # Ejercicio 3.2 - Cuenta cuantos elementos especificos hay dentro de la lista
print("\nEjercicio 3.2\n")
listaFrutas = ["Manzana", "Pera", "Platano", "Naranja"]
listaColores = ["Naranja", "Azul"]
print(listaFrutas)

print("Ejercicio 3.2: ", listaFrutas.count(listaColores[0]))

# # Ejercicio 3.3 - Agrega un elemento dentro de una posicion especificada de una lista.
print("\nEjercicio 3.3\n")
listaFrutas = ["Manzana", "Pera", "Platano", "Naranja"]
print(listaFrutas)
listaFrutas.insert(1,str("Uva"))

print("Ejercicio 3.3: ", listaFrutas)

# # Ejercicio 3.4 - Elimina un elemento de un valor especifico
print("\nEjercicio 3.4\n")
listaFrutas = ["Manzana", "Pera", "Platano", "Naranja"]
print(listaFrutas)
listaFrutas.insert(1,str("Uva"))

print("Ejercicio 3.4: ", listaFrutas)

# # Ejercicio 3.5 - Elimina un elemento en una posicion especifica.
print("\nEjercicio 3.5\n")
listaFrutas = ["Manzana", "Pera", "Platano", "Naranja"]
print(listaFrutas)
listaFrutas.pop(1)

print("Ejercicio 3.5: ", listaFrutas)

# # Ejercicio 3.6 - Ordena una lista
print("\nEjercicio 3.5\n")
listaFrutas = ["Manzana", "Pera", "Platano", "Naranja"]
listaNumeros = [10.2, 5.2, 6.5]
print(listaFrutas)
listaFrutas.sort()


print("Ejercicio 3.5: ", listaFrutas)