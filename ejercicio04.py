"""
Programa que muestre las primeras 5 tablas de multiplicar (la tabla del 1 ,2,3,4,5)
Ejemplo:
1x2=2
2x3=6
3x4=12
5x4=20
"""
print("Tablas de Multiplicar del  1, 2, 3, 4, 5")
print("-" * 12)

for tabla in range(1, 6):
    print(f"\nTabla de Multiplicar del numero  {tabla}:")
    for i in range(1, 11):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")
    print("-" * 20)