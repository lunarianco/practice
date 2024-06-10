"""
27 mayo
#hacer un programa que permita llevar la contabilidad de una panaderia. si las ventas de pan en el dia es mayor
#de 300000, se la da una bonificacion al panadero del 4%, si la ventas de bebidas es mayor de 200000 se le da
#una bonificacion al tendelo del 2%, y si las ventas de postres es mayor de 500000 una bonificacion de 3% al respostero
#el programa debe calcular el total de ventas, de bonificaciones y mostrar discriminadamente el total de las ventas
"""

print ("el pan vale 500, el postre vale 3000 y la bebida vale 2000")
preciopan = float(500)
preciopostre = float(3000)
preciobebida = float(2000)

print("ingrese el numero de panes vendidos")
ventaspandia = float(input())
print("ingrese el numero de postres vendidos")
ventaspostredia = float(input())
print("ingrese el numero de bebidas vendidos")
ventasbebidadia = float(input())

totalpandia = float(ventaspandia*preciopan)
totalpostredia = float(ventaspostredia*preciopostre)
totalbebida = float(ventasbebidadia*preciobebida)

totalventadia = totalpandia+totalpostredia+totalbebida


if totalpandia>300000:
 print("la bonificacion de la paga del panadero es de ",totalpandia*0.04)

 
 if totalbebida>200000:
  print("la bonificacion de la paga del tendero es de ",totalbebida*0.02)
 
  if totalpostredia>500000:
   print("la bonificacion de la paga del repostero es de ",totalbebida*0.03)

print("el total vendido en el dia es de ", totalventadia)   