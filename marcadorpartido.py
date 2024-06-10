"""
Se necesita elaborar un algoritmo que solicite el 
#marcador de un partido de futbol, donde para pasar a los cuadrangulares
#se necesita ganar al menos 30 puntos; sabiendo que ganando son tres puntos,
#perdiendo es cero  y empatando es uno
"""

import time

print("marcador de partido v0.1")
time.sleep(1)
print("ingresar numero de partidos")
partidos = int(input("numero de partidos "))

print("ingresar datos de marcador")
gana = int(input("partidos ganados "))
pierde = int(input("partidos perdidos "))
empat = int(input("partidos empatados "))


winto = gana*3
loseto = pierde*0
draw = empat 
total = winto+draw

print("los resultados de los partidos son los siguientes:")
print("total de partidos: ", partidos)
print("numero de partidos ganados: ", gana, "puntaje de partidos ganados: ", winto)
print("numero de partidos perdidos: ",pierde, "puntaje de partidos perdidos: ", loseto)
print("numero de partidos empatados: ", empat, "puntaje de partidos empatados: ", draw)
print("requiere almenos 30 puntos para clasificar, el puntaje total es de: ", total)



