"""
2.Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor del salario y DNI en consola.
También elimina el key edad de tu diccionario, incluyendo su valor. Mostrar finalmente el diccionario actualizado
"""
diccionario = {'Nombre': 'Estrella','Edad': 34,'salario': 3500,'edad': 34}
lista=list(diccionario.values())
diccionario['DNI']=46466022
print(diccionario)
print(lista)
print(diccionario['salario'],diccionario['DNI'])
del diccionario['edad']
print(diccionario)