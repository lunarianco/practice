"""
calcular secuancia fibonacci de un numero
"""

a = 0 
b = 1
c = 0 #acomulador por eso empieza en cero

num = int(input("ingrse un numero para calcular la secuencia de Fibonacci: "))

for i in range(num+1):
   print(a)
   c = a + b
   a = b
   b = c