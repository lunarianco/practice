"""
Realice un programa que calcule la media de gastos realizados en X 
cantidad de meses definidos (la cantidad de meses se le pregunta al 
usuario y también el valor de gastos de cada mes).
"""

numes = int(input("ingrese la cantidad de meses: "))
monto = 0
gasto = 0
i = 0

for i in range(numes):
    print("________________")
    print("mes %d" %(i+1))
    monto = float(input("ingrese el monto en pesos del mes: "))
    print("mes %d con monto de %f" %(i+1,monto))
    gasto = gasto + monto

media = gasto/numes
print("________________")
print ("la media de gastos de %d mes/meses es de %f pesos." %((i+1),media))    