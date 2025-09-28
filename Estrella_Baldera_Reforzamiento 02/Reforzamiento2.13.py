"""
13. Crea un programa que convierta una temperatura en grados Celsius a
Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
F = (C * 9)/5 + 32
Deberá imprimir algo como lo siguiente:
La temperatura en °C: 30
Temperatura en Fahrenheit: 86.00
Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
variables iniciales para obtener dos temperaturas finales en Fahrenheit)
"""
# Variables de temperatura en grados Celsius
celsius_1 = 30
celsius_2 = 15

# Conversión a Fahrenheit
fahrenheit_1 = (celsius_1 * 9) / 5 + 32
fahrenheit_2 = (celsius_2 * 9) / 5 + 32

# Imprimir resultados
print(f"La temperatura en °C: {celsius_1}")
print(f"Temperatura en Fahrenheit: {fahrenheit_1:.2f}\n")

print(f"La temperatura en °C: {celsius_2}")
print(f"Temperatura en Fahrenheit: {fahrenheit_2:.2f}")
