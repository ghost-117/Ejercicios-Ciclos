'''
Programa que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1
Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador
Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)

'''
print("Este programa calcula la suma y la media de todos los numeros ingresados, cuando se ingresa un 0 termina el programa")


suma = 0
contador = 0
ningresados = []
while True:
    try:
        entrada = input("Introduce un número: ")
        
        # Verificar si la entrada contiene solo dígitos y punto decimal
        if not all(c.isdigit() or c == '.' or (c == '-' and entrada.index(c) == 0) for c in entrada):
            print("Error: Solo se permiten números")
            continue    
        numero = float(entrada)
        
        if numero == 0:
            break 
        # Actualizar suma y contador y almacenamiento de numeros 
        suma += numero
        contador += 1
        ningresados.append(numero)
    except ValueError:  
        print("Error: Entrada inválida. Por favor, introduce un número válido")

if contador > 0:
    media = suma / contador
    print("\nResultados:")
    print(f"\nLa suma total de todos los numeros ingresados es: {suma}")
    print(f"La media es: {media}")
    print(f"Los numeros ingresados son: {ningresados} ")
else:
    print("\nNo se introdujeron números")