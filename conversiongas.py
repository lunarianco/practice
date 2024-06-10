"""
#Construya un diagrama de flujo (DF) que resuelva un problema 
#que tiene una gasolinera. Los dispensadores de esta registran lo 
#que “surten” en galones, pero el precio de la gasolina está fijado
#en litros. El DF debe calcular e imprimir lo que hay que cobrarle 
#al cliente.
"""

print("ingresar el numero de galones")
galo=input()
galop=float(galo)
total = float()
totalgas = float()

if galo == 1:
    total = 15445.99
else:
    totalgas = float(galop*3.78541)
    total = float(totalgas*4080.40)

print ("el precio total es ", round(total,2))  

