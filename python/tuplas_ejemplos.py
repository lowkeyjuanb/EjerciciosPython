# Una tupla en Python es una estructura de datos similar a una lista, pero inmutable.
# Esto significa que, una vez creada, no se puede modificar (agregar, eliminar o cambiar elementos).

# Definiendo una tupla de ejemplo
tupla_ejemplo = ("manzana", "banana", "cereza")
print("Tupla original:", tupla_ejemplo)

# Acceder a elementos de una tupla por índice
print("Primer elemento:", tupla_ejemplo[0])  # Salida: manzana
print("Último elemento:", tupla_ejemplo[-1])  # Salida: cereza

# Desempaquetar una tupla (asignar sus valores a variables)
fruta1, fruta2, fruta3 = tupla_ejemplo
print("Frutas desempaquetadas:", fruta1, fruta2, fruta3)

# Intentar modificar una tupla generará un error
# tupla_ejemplo[0] = "pera"  # Esto daría un error, ya que las tuplas son inmutables

# Concatenar tuplas
nueva_tupla = tupla_ejemplo + ("uva", "naranja")
print("Tupla concatenada:", nueva_tupla)

# Repetir una tupla
repetida = tupla_ejemplo * 2
print("Tupla repetida:", repetida)

# Verificar si un elemento está en la tupla
if "banana" in tupla_ejemplo:
    print("'banana' está en la tupla")

# Obtener la longitud de una tupla
print("Longitud de la tupla:", len(tupla_ejemplo))

# Contar cuántas veces aparece un elemento en la tupla
tupla_numeros = (1, 2, 3, 1, 2, 1)
print("Número de veces que aparece 1:", tupla_numeros.count(1))

# Obtener el índice de un elemento en la tupla
print("Índice de 'cereza':", tupla_ejemplo.index("cereza"))