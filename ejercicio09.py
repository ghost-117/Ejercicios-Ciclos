'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
while True:
    try:
        liminferior = int(input("Introduce el límite inferior: "))
        limsuperior = int(input("Introduce el límite superior: "))
        
        if liminferior < limsuperior:
            break
        print("Error: El límite inferior debe ser menor que el límite superior")
    except ValueError:
        print("Error: Introduce un número entero válido")

sumadenumintervalo = 0
numfueraintervalo = 0
numigualimites = 0
while True:
    try:
        numero = int(input("Introduce un número (0 para terminar): "))
        
        if numero == 0:
            break
        
        if numero == liminferior or numero == limsuperior:
            numigualimites += 1
        
        if liminferior < numero < limsuperior:
            sumadenumintervalo += numero
        else:
            numfueraintervalo += 1
    
    except ValueError:
        print("Error: Introduce un número entero válido")
        
print(f"\n Resultados:")
print(f"Suma de números dentro del intervalo ({liminferior}, {limsuperior}): {sumadenumintervalo}")
print(f"Números fuera del intervalo: {numigualimites}")
