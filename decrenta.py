
"""
Los tramos impositivos para la declaración de la renta en un 
determinado país son los siguientes:
1. menos de 10.000€  --->> 5%
2  Entre 10.000€ y 20.000€ --->> 15%
3. Entre 20.000€ y 35.000€ --->> 20%
4. Entre 35.000€ y 60.000€ --->> 30%
5. Más de 60.000€ --->> 45%
Escribir un programa que pregunte al usuario su renta anual y 
muestre por pantalla el tipo impositivo que le corresponde.
"""

porcentaje = float()
renta = float(input("ingrese su renta en euros: "))


def total(renta):
    return renta*porcentaje/100


if renta >= 0 and renta <10000:
    porcentaje = 5
    print(renta, " euros ingresados, su tramo impositivo es del 5% y equivale a" )
elif renta >= 10000 and renta <20000: 
    porcentaje = 15  
    print(renta," euros ingresados, su tramo impositivo es del 15% y equivale a")
elif renta >= 20000 and renta <35000:   
    porcentaje = 20
    print(renta, " euros ingresados, su tramo impositivo es del 20% y equivale a")
elif renta >= 35000 and renta <60000:  
    porcentaje = 30 
    print(renta," euros ingresados, su tramo impositivo es del 30% y equivale a")
elif renta > 60000:   
    porcentaje = 45
    print(renta," euros ingresados, su tramo impositivo es del 45% y equivale a")
else:
    print("ingrese una renta valida")    


print(total(renta), "€")