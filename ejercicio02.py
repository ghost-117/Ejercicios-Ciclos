'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''

import random

# Generar número aleatorio entre 1 y 100
numrandom = random.randint(1, 100)
intentos = 10
adivinado = False

print("Adivina un número entre 1 y 100")
print("Tienes 10 intentos para adivinarlo")

while intentos > 0 and not adivinado:
    print(f"\nTe quedan {intentos} intentos")
    numero = int(input("Ingresa un número entero: "))
    if numero == numrandom:
        adivinado = True
    elif numero < numrandom:
        print( f"El  número secreto es MAYOR que el {numero}")
    else:
        print( f"El número secreto es MENOR que el {numero}")
        
    intentos -= 1
if adivinado:
    print(f"\n¡Felicitaciones! Has adivinado el número en {10 - intentos} intentos")
else:
    print(f"\nLo siento, te has quedado sin intentos. El número era {numrandom}")