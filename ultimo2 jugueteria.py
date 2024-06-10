"""
Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea 
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

pesopaya=float(112)
pesomune=float(75)
print("********************")
print("el precio por kilo es de 50000 pesos")
print("********************")
print("ingrese la cantidad de payasos a pedir")
numpaya=float(input())
print("ingrese la cantidad de munecas a pedir")
nummune=float(input())

totalpaya=pesopaya*numpaya
totalmune=pesomune*nummune

print("peso total de payasos ", totalpaya, "gramos")
print("peso total de munecas ", totalmune, "gramos")


pesototal = totalpaya + totalmune 
print("peso total en gramos es de ", pesototal)
pesototalkilo = float(pesototal / 1000)
print("peso total en kilos es de ", pesototalkilo)

preciopaquete = float(pesototalkilo* 50000)

print("el costo del paquete es de ", preciopaquete, "pesos")