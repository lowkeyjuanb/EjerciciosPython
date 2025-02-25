# DICCIONARIOS 

# Estos son utilizados para guardar información en un formato de pares key:value.
# Es una colección ordenada, cambiable, y no permite duplicados.


# Se escriben de la siguiente manera:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("EJEMPLO DE DICCIONARIO: ", thisdict)
print("\n")

# Los valores guardados pueden ser llamados a partir de sus llaves (keys)

print(thisdict["brand"])

# Son ordenados porque sus valores tienen un orden definido, el cual no cambiara.

# Son cambiables porque puedes modificar, agregar o eliminar datos después de crear el diccionario.

# Ademas, no permite duplicados de una misma llave.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("EJEMPLO LLAVE DUPLICADA: ",thisdict)
print("\n")

# Puedes determinar cuantos valores hay dentro de un diccionario usando len()

print("LENGTH de un DIC: ",len(thisdict))
print("\n")

# Puedes agregar distintos tipos de datos
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

# Al igual que los otros tipos de datos, puedes usar un constructor dict()
thisdict = dict(name = "John", age = 36, country = "Norway")
print("Diccionario con constructor: ", thisdict)
print("\n")


# Definiendo un diccionario básico con datos de una persona
diccionario_persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a un valor usando su clave
print("Nombre: ", diccionario_persona["nombre"])  # Salida: Juan

# Otra forma de acceder a un valor usando get() (evita errores si la clave no existe)
edad = diccionario_persona.get("edad")
print("Edad: ", edad)  # Salida: 25

# Agregar un nuevo par clave-valor al diccionario
diccionario_persona["profesion"] = "Ingeniero"
print("Diccionario actualizado: ", diccionario_persona)

# Modificar un valor existente
diccionario_persona["ciudad"] = "Barcelona"
print("Nueva ciudad: ", diccionario_persona["ciudad"])  # Salida: Barcelona

# Eliminar una clave del diccionario usando del
del diccionario_persona["edad"]
print("Diccionario tras eliminar edad: ", diccionario_persona)

# Recorrer un diccionario con un bucle for
for clave, valor in diccionario_persona.items():
    print(clave, "->", valor)

# Verificar si una clave existe en el diccionario
if "nombre" in diccionario_persona:
    print("La clave 'nombre' existe en el diccionario.")

# Obtener todas las claves
diccionario_claves = diccionario_persona.keys()
print("Claves del diccionario: ", diccionario_claves)

# Obtener todos los valores
diccionario_valores = diccionario_persona.values()
print("Valores del diccionario: ", diccionario_valores)

# Vaciar un diccionario
diccionario_persona.clear()
print("Diccionario vacío: ", diccionario_persona)  # Salida: {}


