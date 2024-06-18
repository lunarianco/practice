"""
programa que muestra las tablas del 1 al 10 completas
"""

tabla = 1
inc = 1

for tabla in range (1,11):
    print("--------------------")    
    print("la tabla del ",tabla, "\n")
    for inc in range (1,11):
        print(tabla, " x ", inc, " = ",tabla*inc)
