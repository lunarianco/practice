"""
#Si tengo una X cantidad de pesos, dar su equivalente en dólares 
#y después en euros. Se sabe que 1 dólar =3800  pesos y 1 
#euro=4200 pesos.
"""

print("el monto en pesos")
peso=input()
pesop=float(peso)

dolar = pesop/3800
euro = pesop/4200

print("el equivalente de ", pesop, " en dolares es de ", round(dolar, 4), " y en euros es de ", round(euro,4))