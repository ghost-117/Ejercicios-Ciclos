'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''
while True:
    try:
        base = float(input("Ingrese la base: "))
        break
    except ValueError:
        print("Error: Por favor ingrese un número válido")
while True:
    try:
        exponente = int(input("Ingrese el exponente ( numero entero positivo): "))
        if exponente < 0:
            print("Error: El exponente debe ser positivo")
        break
    except ValueError:
        print("Error: Por favor ingrese un número entero")

resultado = 1
for i in range(exponente):
    resultado *= base
print(f"{base} elevado a la {exponente} es: {resultado}")