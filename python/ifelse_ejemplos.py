# Las estructuras condicionales if, elif y else permiten ejecutar código dependiendo de condiciones lógicas.

# Ejemplo básico de if
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")  # Se ejecuta si la condición es verdadera

# Uso de if-else
hora = 14
if hora < 12:
    print("Buenos días")
else:
    print("Buenas tardes")

# Uso de if-elif-else
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")

# Condición múltiple con operadores lógicos
usuario_activo = True
es_admin = False
if usuario_activo and es_admin:
    print("Acceso total al sistema")
elif usuario_activo:
    print("Acceso limitado")
else:
    print("Acceso denegado")

# Uso de if en una sola línea (operador ternario)
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

# Verificar si un valor está en una lista con if
frutas = ["manzana", "banana", "cereza"]
if "banana" in frutas:
    print("La banana está en la lista de frutas")
