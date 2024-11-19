'''
Programa que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
print("\n== Programa que  identifica las Vocales ==")
print("Introduce un carácter o un espacio para terminar el programa")
print("--" * 20)
conta=0

while True:
    caracter = input("\nIntroduce un carácter: ").lower()
    
    if caracter == " " :
        print("\n¡Programa terminado!")
        print(f"\nTotal de caracteres introducidos: {conta}")
        break
    conta += 1
    if caracter in "aeiouáéíóú":
        print(f"La letra {caracter} SI es Vocal")
        resultado = "Vocal"
    else:
        print(f"La letra {caracter} NO es Vocal")
        resultado = "No Vocal"