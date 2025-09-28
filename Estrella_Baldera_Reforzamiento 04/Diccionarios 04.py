""""
4.Crear un diccionario con 6 departamentos del país.
-
Borrar cualquier departamento, usando la palabra reservada del.
-
Actualizar el penúltimo departamento por otro.
-
Comprobar que no existe este departamento borrado dentro del diccionario.\
"""
# Crear diccionario con 6 departamentos diferentes
departamentos = {'A': 'Tacna','B': 'Moquegua', 'C': 'Cusco', 'D': 'Puno', 'E': 'Ayacucho', 'F': 'Huancavelica'}

print("Diccionario inicial:", departamentos)

# Borrar un departamento (ejemplo: clave 'C')
del departamentos['C']

# Verificar que ya no existe la clave 'C'
print("¿Existe 'C' en el diccionario?:", 'C' in departamentos)

# Convertir claves a lista para identificar el penúltimo
lista1 = list(departamentos.keys())
clave_penultimo = lista1[-2]

# Actualizar el penúltimo departamento
departamentos[clave_penultimo] = 'Madre de Dios'

print("Diccionario final:", departamentos)
