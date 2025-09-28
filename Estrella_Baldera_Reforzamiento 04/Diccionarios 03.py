"""
3.Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes.
"""
diccionario = {'Nombre': 'Estrella','Edad': 34,'salario': 3500,'edad': 34}
lista=list(diccionario.values())
diccionario['DNI']=46466022
print(diccionario)
print(lista)