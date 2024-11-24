'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
ahorroT = 0
AhorroTmensual = 0

for mes in range(1, 13):
    Ahomes = float(input(f"Ingrese ahorro para el mes {mes}: "))
    
    ahorroT += Ahomes
    AhorroTmensual += Ahomes
    
    print(f"Ahorro acumulado al mes {mes}: {AhorroTmensual}")

print(f"\nAhorro total en el año: {ahorroT}")