# # Las estructuras condicionales if, elif y else 
# # permiten ejecutar código dependiendo de condiciones lógicas.

# # Ejemplo básico de if
# print("EJEMPLO 1")
# edad = 13
# if edad >= 18:
#     print("Eres mayor de edad.")  # Se ejecuta si la condición es verdadera

# # Uso de if-else
# print("EJEMPLO 2")
# hora = 12
# if hora < 12:
#     print("Buenos días")
# else:
#     print("Buenas tardes")

# Uso de if-elif-else
# print("EJEMPLO 3")
# nota = 8
# if nota >= 90:
#     print("Excelente")
# elif nota >= 80:
#     print("Muy bien")
# elif nota >= 70:
#     print("Bien")
# else:
#     print("Necesitas mejorar")

# Condición múltiple con operadores lógicos
# AND - Ambas condiciones tienen que cumplirse.
# OR - Una condicion tiene que cumplirse.

# # print("EJEMPLO 4")
# usuarioActivo = True
# esAdmin = False

# if usuarioActivo and esAdmin:
#     print("Acceso total al sistema")
# elif usuarioActivo:
#     print("Acceso limitado")
# else:
#     print("Acceso denegado")

# # Uso de if en una sola línea (operador ternario)
# print("EJEMPLO 5")
# edad = 15
# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
# print(mensaje)

# Verificar si un valor está en una lista con if
print("EJEMPLO 6")
frutas = ["manzana", "banana", "cereza", "pera"]
if "pera" in frutas:
    print("La pera está en la lista de frutas")

# Buenas practicas 

if "pera" in frutas and "banana" in frutas:
    print("Hay peras y bananas")
