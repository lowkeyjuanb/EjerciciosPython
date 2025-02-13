# Listas 

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
listaAlcohol = ["Tequila", "Vodka", "Whisky", "Ron"]

print("Accesa a n elemento dentro de una lista:", listaAlcohol[0])

print("Accesa al ULTIMO elemento de una lista:", listaAlcohol[-1])

print("Accesa a un rango de elementos dentro de una lista:", listaAlcohol[1:3])

print("Imprime los elementos desde el primero hasta n dato:", listaAlcohol[:2])

# Ejemplo con condicionales:

if "Tequila" in listaAlcohol:
    print("Si esta el elemento Tequila en listaAlcohol")


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


# Ejercicio 3.1 - Agrega un elemento al final de una lista

# Ejercicio 3.2 - Cuenta cuantos elementos hay dentro de la lista

# Ejercicio 3.3 - Agrega un elemento dentro de una posicion especificada de una lista.

# Ejercicio 3.4 - Elimina un elemento de un valor especifico

# Ejercicio 3.5 - Elimina un elemento en una posicion especifica.

# Ejercicio 3.6 - Ordena una lista
