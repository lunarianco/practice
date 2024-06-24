"""
En una empresa trabajan N cantidad de empleados cuyos sueldos oscilan 
entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado 
e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""
empleados = int(input("ingrese la cantidad de empleados: "))
sueldo = float(0)
sueldo100 = float(0)
sueldo300 = float(0)

menos300 = 0
mas300 = 0
i = 0

if empleados <= 0:
    print ("ingrese un numero valido de empleados")
    exit()

for i in range(empleados):
    print("________________")
    print("empleado %d" %(i+1))
    sueldo= float(input("ingresar un salario entre 100 o 500 $: "))
    if sueldo >= 100 and sueldo <= 500:
        if sueldo >= 100 and sueldo < 300:
            menos300 += 1
            sueldo100 = sueldo100 + sueldo
        else:
            mas300 += 1
            sueldo300 = sueldo300 + sueldo

    else:
        print("ingrese un salario valido entre 100 y 500")
        exit()            
    
print("##############")
print ("numero de empleados que cobran menos de 300 es %d, numero de empleados que cobran mas de 300 es %d." %(menos300,mas300)) 
print ("el importe gastado en salarios inferiores a 300 es de %f $, el importe gastado en salarios superiores a 300 es de %f $" %(sueldo100,sueldo300))      
print ("el importe gastado en salarios totales es de %f $" %(sueldo100 + sueldo300)) 