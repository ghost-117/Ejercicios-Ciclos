'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
# Versión profesional usando for y range
print("\n=== Buscador de Números Pares ===")
print("=" * 40)

# Obtener y validar la entrada del usuario
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    inicio = min(num1, num2)
    fin = max(num1, num2)

    if inicio % 2 != 0:
        inicio += 1
        
    print("-" * 40)
    print(f"Rango analizado: {min(num1, num2)} a {max(num1, num2)}")

    pares = []
    for numero in range(inicio, fin +1 ,2):
        pares.append(numero)
    if pares:
        print("\nNúmeros pares encontrados:")
        for i in range(0, len(pares), 10):
            print(*pares[i:i+10], separacion="\t")
        print(f"\nTotal de números pares: {len(pares)}")
    else:
        print("\nNo se encontraron números pares en el rango especificado")
    
except ValueError:
    print("\nError: Por favor ingrese solo números enteros")

print("\n" + "=" * 30)