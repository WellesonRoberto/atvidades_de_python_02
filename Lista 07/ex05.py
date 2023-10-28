'''Crie um programa que utilize o Broadcasting do NumPy para converter as
temperaturas registradas em graus Celsius para Fahrenheit e Kelvin. '''
import numpy as np

print("\nTemperaturas em Celsius:")
temp_celsius = np.array([25, 28, 35, 29, 31.5, 32.6, 37])
print(temp_celsius)
print()
temp_fahrenheit = []
temp_kelvin = []

# Convertendo Celsius para Fahrenheit
fahrenheint = temp_celsius * 1.8 + 32
temp_fahrenheit.append(fahrenheint)
temp_fahrenheit = np.array(temp_fahrenheit)
print("\nTemperaturas em Fahrenheint:")
print(temp_fahrenheit)
print()

# Convertendo Celsius para Kelvin
kelvin = temp_celsius + 273
temp_kelvin.append(kelvin)
temp_kelvin = np.array(temp_kelvin)
print("\nTemperaturas em Kelvin:")
print(temp_kelvin)
print()
