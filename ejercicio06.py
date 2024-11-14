'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
print("Calculadora de Promedio al ingresar 10 números")
print("-" * 20)

numeros = [] 
suma = 0
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
    suma += numero
promedio = suma / 10

#Resultados
print("\nResultados:")
print("-" * 30)
print(f"Los números ingresados son: {numeros}")
print(f"La suma total de los numeros son: {suma}")
print(f"El promedio es: {promedio}")