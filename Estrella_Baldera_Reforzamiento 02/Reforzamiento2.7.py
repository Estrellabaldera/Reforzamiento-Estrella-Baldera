"""
7.De 3 números asignados mayores a 30 (entre positivos y negativos tú los
propones) a 3 variables, se pide hallar la suma de los valores de los módulos
con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.
"""
var1 = 535
var2 = -25
var3 = 100

# Cálculo de los módulos
modulo_con_3 = var1 % 3
modulo_con_5 = var2 % 5
modulo_con_7 = var3 % 7
suma_modulos = modulo_con_3 + modulo_con_5 + modulo_con_7
print("Módulo 3 es:",modulo_con_3)
print("Módulo 5 es:",modulo_con_5)
print("Módulo 7 es:",modulo_con_7)
print(f"La suma de los valores de los módulos es: {suma_modulos}")
