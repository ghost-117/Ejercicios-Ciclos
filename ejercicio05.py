'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''
print("Calculadora de Promedio - Ingresa 10 números")
print("-" * 20)

numeros = []  
suma = 0
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    suma += numero
promedio = suma / 10
print("\nResultados:")
print("-" * 30)
print(f"Los números ingresados son: {numeros}")
print(f"La suma totalde los numeros es: {suma}")
print(f"El promedio es: {promedio}")