'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''
while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("Error: Introduce un número no negativo")
            continue
        break
    except ValueError:
        print("Error: Introduce un número válido")

Nprimo = 0
if numero > 1:
    divisor = 1
    Rcuadrada = int(numero**0.5) + 1
    
    while divisor < Rcuadrada:
        if numero % divisor == 0:
            Nprimo += 1
        divisor += 1
if numero <= 1:
    print(f"• {numero} no es primo por definición")
elif Nprimo == 1:
    print(f" {numero} es un número primo")
    print("   No tiene divisores diferentes a 1 y sí mismo")
else:
    print(f" {numero} no es un número primo")
    print(f"  Es divisible por {divisor}")