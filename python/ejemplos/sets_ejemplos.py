# Un SET en Python es una colección desordenada de elementos únicos.
# No permite elementos duplicados y es útil para operaciones como la eliminación de duplicados o pruebas de pertenencia rápidas.

# Definiendo un set de ejemplo
set_ejemplo = {"manzana", "banana", "cereza"}

print("Set original:", set_ejemplo)

# Agregar un elemento a un set
# set_ejemplo.add("uva")
# print("Set después de agregar 'uva':", set_ejemplo)

# # Intentar agregar un elemento duplicado no tiene efecto
# set_ejemplo.add("manzana")
# print("Set después de intentar agregar 'manzana' nuevamente:", set_ejemplo)

# Eliminar un elemento de un set
# set_ejemplo.remove("banana")  # Generará un error si el elemento no existe
# print("Set después de eliminar 'banana':", set_ejemplo)

# Eliminar un elemento de forma segura con discard (no genera error si no existe)
# set_ejemplo.discard("pera")
# print("Set después de intentar descartar 'pera':", set_ejemplo)

# Unir dos sets con la operación de unión
otro_set = {12, 32, 2}
print(set_ejemplo | otro_set)

# También se puede usar set_ejemplo.union(otro_set)
print("Set original:", set_ejemplo)

# Encontrar la intersección entre dos sets (elementos en común)
# interseccion_set = set_ejemplo & otro_set  # También se puede usar set_ejemplo.intersection(otro_set)
# print("Intersección de sets:", interseccion_set)

# # Encontrar la diferencia entre dos sets (elementos en set_ejemplo que no están en otro_set)
# diferencia_set = set_ejemplo - otro_set  # También se puede usar set_ejemplo.difference(otro_set)
# print("Diferencia de sets:", diferencia_set)

# # Verificar si un elemento está en un set
# if "cereza" in set_ejemplo:
#     print("'cereza' está en el set")

# # Obtener la cantidad de elementos en un set
# print("Tamaño del set:", len(set_ejemplo))

# # Vaciar un set
# set_ejemplo.clear()
# print("Set vacío:", set_ejemplo)
