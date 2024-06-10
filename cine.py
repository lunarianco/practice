"""
27 mayo
###juan va al cine, y encuentra un cartel diciendo: los lunes, miercoles y viernes las entradas cuestan 10.000 pesos
#los martes y jueves las entradas cuestan 8.000 pesos,
#los sabados y domingos cuestan las entradas 12.000 pesos. juan quiere hacer una reserva
###hacer un programa donde le indique el nombre, numero de silla, sala de cine, cantidad de tickets, y el valor total a pagar, teniendo en cuenta
###que si la reserva fue telefonica costara un adicional de 4% pero si es por la via web, costara un adicional de 2%
"""
import random

nombre = "juan"

lunmievie = 10000
marjue = 8000
sabdom = 12000

filasilla = ["a","b","c","d","e"]
columnasilla = ["1","2","3","4","5"]
salacine = ["A","B","C","D"]
diasemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

print("ingrese su tipo de reservacion 1 para telefonica, 2 para internet")
reserva=int(input())
print("ingrese el dia en el que le gustaria reservar los tickets")
print("0 lunes, 1 martes, 2 miercoles, 3 jueves, 4 viernes, 5 sabado, 6 domingo")
dia = int(input())
print("ingrese cantidad de tickets a comprar")
numtick=int(input())

print("*****************")
print ("su nombre es", nombre)
print ("la sala de cine asignada es: ", "\n", salacine[random.randint(0,3)])
print ("su silla asignada es")
print(filasilla[random.randint(0,4)], columnasilla[random.randint(0,4)])
print ("el dia elegido es:", diasemana[dia])

if diasemana[dia] == "lunes" or diasemana[dia] =="miercoles" or diasemana[dia] =="viernes":
    if reserva == 1:
     print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*lunmievie+(numtick*lunmievie*0.04))
    else: 
         if reserva == 2:
            print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*lunmievie+(numtick*lunmievie*0.02))

else:
    if diasemana[dia] == "martes" or diasemana[dia] == "jueves":
            if reserva == 1:
             print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*marjue+(numtick*marjue*0.04))
            else:
                if reserva == 2:
                 print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*marjue+(numtick*marjue*0.02))

    else:
            if diasemana[dia] == "sabado" or diasemana[dia] == "domingo":
                        if reserva == 1:
                         print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*sabdom+(numtick*sabdom*0.04))
                        else: 
                            if reserva == 2:
                             print ("cantidad de tickets es de ", numtick, " y su valor es de ", numtick*sabdom+(numtick*sabdom*0.02))





#print (filasilla[0])

