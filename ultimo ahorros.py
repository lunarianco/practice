"""
imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
segundo y tercer años. Redondear cada cantidad a dos decimales


"""
print("ingrese el monto anual")
ahorro = float(input())
porcentaje = float(ahorro*0.04)
ahorro1 = ahorro + porcentaje
ahorro2 = ahorro1 + porcentaje
ahorro3 = ahorro2 + porcentaje

print("la cantidad de ahorros para el primer periodo annual es de ", ahorro1)
print("la cantidad de ahorros para el segundo periodo annual es de ", ahorro2)
print("la cantidad de ahorros para el tercer periodo annual es de ", ahorro3)