"""
Permite realizar una serie de inmstrucciones una cantidad determinada de veces
Estructura:
for i in [1..n]
instrucciones
range (fin)
    range(3)    [0,1,2]
range (incio, fin)
    range(4, 7) [4,5,6]
range (inicio, fin ,pasos)
    (2,9,2) [2,4,6,8]
"""
#Ejemplo: Inmprimir los numeros del 1 al 10
print("Programa que imprime los primeros 10 numeros y de vuelta ")
for i in range(10):
   print(f"Num: {i + 1} vuelta {i}")
   print( "" * 3)
    
    #Ejemplo: Inmprimir los numeros del 10 al 20
print("Programa que imprime los numeros de un rango de 10 a 20")
for i in range(10, 21):
    print(f"Numero: {i + 1}")
    print( "" * 3)
    
    #Imprimir los numeros pares del 0 al 20
    print("Programa que imprime los numeros pares del 0 al 20")
    for i in range ( 0, 21, 2 ):
       print(f"Numero: {i}")
    print( "" * 3)
        
#Imprimir la tabla completa  de multiplicar de un numero  leido desde el teclado, 
num = int(input("Ingresa un número: "))
for i in range(1, 11):
    print(f" La tabla de multiplicar del {num}  es {num} x {i}  = {num * i}") 

