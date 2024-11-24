'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
Pactual = 10
mesestotales = 20
total_pagado = 0
Pinicial= 10
for mes in range(1, 21):
    print(f"En el Mes {mes}:Pago  \t {Pactual} euros")
    total_pagado += Pactual
    Pactual *= 2
    porcentaje_progreso = (mes / mesestotales) * 100
    print(f"\n • Progreso del plan: {porcentaje_progreso:.1f}%")


print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")
print(f" Último pago: {Pactual/2} euros")
print(f" Primer pago: {Pinicial} euros")
print(f"• Promedio mensual: {total_pagado / mesestotales} euros")