"""
Hacer un programa que lea N números 
(la cantidad la ingresa el usuario),
 calcule y muestre la suma de los pares 
 y el producto de los impares.
 """
numero = int(input("ingrese un numero o un 0 para parar: "))
contpar = 0
contimpar = 0
sumapar = 0
proimpar = 1

while numero != 0:
    if numero % 2 == 0:
        contpar += 1
        sumapar = sumapar + numero
    else:
        contimpar += 1
        proimpar = proimpar * numero
    
    numero = int(input("ingrese un numero o un 0 para parar "))   

if proimpar == 1:
    proimpar = 0

print ("################")
print ("los pares totales ingresados son ", contpar)      
print ("los impares totales ingresados son ", contimpar)       
print ("la suma de los pares es de %d y el producto de los impares es de %d " %(sumapar, proimpar))