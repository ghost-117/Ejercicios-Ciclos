'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
n = int(input("¿Cuántos números primos quieres mostrar?: "))
numeros_encontrados = 0
numero = 2

# Usar while para encontrar los N números primos
while numeros_encontrados < n:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(" \nLos numeros primos encontrados son:")
        print(numero, end="")
        numeros_encontrados += 1
    
    numero += 1