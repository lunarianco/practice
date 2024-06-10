"""
solicitar el nombre y la edad del usuario y
 con esto decir si el usuario pertenece a primera 
 infancia(0-5), infancia(6-13), juventud(14-23), 
 adultez(24-50) o vejez(>50).
"""

nombre = input("ingrese su nombre ")
edad = int(input("ingrese su edad "))

if edad >= 0 and edad <=5:
    print(nombre,"de ", edad, " pertenece a la primera infancia")
elif edad >= 6 and edad <=13:   
    print(nombre,"de ", edad," pertenece a la infancia")
elif edad >= 14 and edad <=23:   
    print(nombre,"de ", edad," pertenece a la juventud")
elif edad >= 24 and edad <=50:   
    print(nombre,"de ", edad," pertenece a la adultez")
elif edad > 50 and edad <=150:   
    print(nombre,"de ", edad," pertenece a la vejez")
else:
    print("ingrese una edad valida")    
