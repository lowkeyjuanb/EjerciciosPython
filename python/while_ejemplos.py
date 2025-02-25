# Los bucles while en Python permiten ejecutar un bloque de código repetidamente
# mientras una condición se mantenga verdadera.

# Ejemplo básico de while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementamos el contador para evitar un bucle infinito

# Uso de break para salir del bucle
numero = 1
while numero <= 10:
    print("Número:", numero)
    if numero == 5:
        print("Se alcanzó el número 5, saliendo del bucle.")
        break  # Termina el bucle aunque la condición siga siendo verdadera
    numero += 1

# Uso de continue para saltar una iteración
numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        print("Saltando el número 3")
        continue  # Omite el resto del código en esta iteración y pasa a la siguiente
    print("Número:", numero)

# Uso de else con while
intentos = 0
clave_correcta = "python123"
while intentos < 3:
    clave = input("Introduce la clave: ")
    if clave == clave_correcta:
        print("Acceso concedido")
        break
    intentos += 1
else:
    print("Demasiados intentos, acceso denegado")
