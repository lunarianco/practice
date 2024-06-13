"""
Implemente un código con dos contadores, 
uno para números pares y otro para números impares, 
ahora haga que el usuario ingrese tantos números como desee 
y sume a cada contador cuando corresponda, 
recuerde definir la condición de parada, 
por ejemplo, cuando se ingrese 0.
"""

numero = int(input("ingrese un numero o un 0 para parar "))
contpar = 0
contimpar = 0

while numero != 0:
    if numero % 2 == 0:
        contpar += 1
       # numero = int(input("ingrese un numero o un 0 para parar "))
    #elif numero % 2 != 0:
    else:
        contimpar += 1
       # numero = int(input("ingrese un numero o un 0 para parar "))
    numero = int(input("ingrese un numero o un 0 para parar "))   

print ("los pares totales ingresados son ", contpar)      
print ("los impares totales ingresados son ", contimpar)            



