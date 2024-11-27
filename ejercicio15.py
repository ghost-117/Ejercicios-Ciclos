'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''

binario = ""
while True:
    
    try:
        numero = int(input("Introduce un número entero: "))
        break
    except ValueError:
        print("Error: Por favor, introduce un número entero válido")

while numero > 0:
    
    residuo = numero % 2
    binario = str(residuo) + binario
    numero = numero // 2

print(f"El número {numero} en binario es: {binario}")              
        
        