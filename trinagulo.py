"""
#Si se conoce la longitud de dos de los lados de un triángulo (b y c) y el ángulo entre ellos (alfa), expresado en grados 
#sexagesimales, la longitud del tercer lado (a) se calcula por la fórmula:
a^2 = c^2 + b^2 - 2 cb (cos A) 
"""
import math


print("ingresar longitud del lado b")
b=float (input())
print("ingresar longitud del lado c")
c=float (input())
a=float (0)

print("ingresar la medida en grados del angulo alfa")
alfa= float(input())

a2 = b*b + c*c - (2*b*c * (math.cos(alfa)))
#z2 = 25**2 + 30**2 - 2*25*30 * (math.cos(30))  usando como valores b 30, c 25 y alfa 30
#z = math.sqrt(z2)  35.96696852903541  pero segun las calculadoras en linea tiene que dar 15.032    https://www.mathepower.com/es/triangulo.php
a = math.sqrt(a2)

print("la longitud del lado a es de ", a)