"""
1.	Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos) Reglas:
-	Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
-	Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una conversión de datos
-	Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted tiene un bono del 5% en el mes diciembre”
-	Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda.
"""
#Asignar en variables los datos
nombre = "Estrella"
salario = 3500.0
edad = "34"
compania = "Miski Mayo"

#Convertir edad de string a entero
edad_int = int(edad)

#Verificar condición de edad y mostrar mensaje
if edad_int > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono = (salario ** 2) + (salario * 0.10)
else:
    print("Usted tiene un bono del 5% en el mes de diciembre")
    bono = (salario ** 2) + (salario * 0.05)

#Mostrar el bono final
print(f"El bono final es: {bono}")
