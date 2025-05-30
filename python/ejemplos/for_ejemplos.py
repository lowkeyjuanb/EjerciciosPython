# Los bucles for en Python se utilizan para iterar sobre secuencias como listas, tuplas, cadenas y rangos.
# Ejemplo básico: recorrer una lista de frutas
print("EJEMPLO 1")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

# Usando range() para generar una secuencia de números
print("EJEMPLO 2")
for numero in range(5):  # Genera números del 0 al 4
    print("Número:", numero)

# Especificando un rango con inicio y fin
print("EJEMPLO 3")
for numero in range(2, 6):  # Genera números del 2 al 5
    print("Número en rango(2,6):", numero)

# Usando un paso en range()
print("EJEMPLO 4")
for numero in range(0, 10, 2):  # Números del 0 al 8 con paso de 2
    print("Número con paso 2:", numero)

# Iterando sobre una cadena de texto
print("EJEMPLO 5")
palabra = "Python"
for letra in palabra:
    print("Letra:", letra)

# Uso de break para salir del bucle
print("EJEMPLO 6")
for numero in range(10):
    if numero == 5:
        print("Se alcanzó el 5, saliendo del bucle.")
        break
    print("Número:", numero)

# Uso de continue para saltar una iteración
print("EJEMPLO 7")
for numero in range(5):
    if numero == 2:
        print("Saltando el número 2")
        continue
    print("Número:", numero)

# Usando else con for
print("EJEMPLO 8")
for numero in range(3):
    print("Número en for:", numero)
else:
    print("Bucle finalizado sin interrupciones")
