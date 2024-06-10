"""
27 mayo
#hacer un programa donde un obrero gana por hora, el valor de la hora depende del cargo
#si es fontanero, gana 7000 la hora, si es albañil gana 7300 la hora, y si es maestro de obra
#gana alrededor de 8500 la hora. si se labora en un dia 8 horas, cuanto sera el salario del obrero trabajando 24 dias
#al mes, descontando la ss del 8%. el programa debe mostrar el nombre del obrero, su profesion y su valor hora y su salario mensual
"""

sldfonthora = float(7000)
sldalbahora = float(7300)
sldmaestrehora = float(8500)    #variables que guardan el valor de la hora

fontdia = float(sldfonthora*8)
albadia = float(sldalbahora*8)
maestredia = float(sldmaestrehora*8)    #variables que guardan el valor del dia laboral

font24 = float(fontdia*24)
alba24 = float(albadia*24)
maestre24 = float(maestredia*8)     #variables que guardan el valor del mes

ssfont = float(font24 - font24*0.08)
ssalba = float(alba24 - alba24*0.08)
ssmaestre = float(maestre24 - maestre24*0.08)       #variables que guardan el valor del mes descontando seguridad social

print("por favor ingrese el nombre del obrero")
nombre = str(input())
print ("puede elejir en cargo: 1 para fontanero, 2 para albanil o 3 para maestro")
print("ingrese el cargo de ", nombre)
cargo = int(input())

if cargo == 1:
    print("el nombre del obrero es", nombre, "\nel cargo es fontanero\nsu valor por hora es de", sldfonthora, "\nsu salario mensual descontando salud social es de", ssfont)
if cargo == 2:
           print("el nombre del obrero es", nombre, "\nel cargo es albañil\nsu valor por hora es de", sldalbahora, "\nsu salario mensual descontando salud social es de", ssalba)
if cargo == 3:
               print("el nombre del obrero es", nombre, "\nel cargo es maestro de obra\nsu valor por hora es de", sldmaestrehora, "\nsu salario mensual descontando salud social es de", ssmaestre)
else: False
