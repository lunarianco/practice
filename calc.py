import time

print("calculadora basica v0.1")
time.sleep(1)
print("ingresar dos numeros...")
time.sleep(1)
num1 = float(input("primer numero a operar "))
num2 = float(input("segundo numero a operar "))

print("\nseleccione la operacion...")
print("a para suma")
print("b para resta")
print("c para multiplicacion")
print("d para division")
eleccion = input ("\nelija entre a,b,c,d: ")
time.sleep(1)

match eleccion:
    case "a":
        print (num1+num2)
    case "b":
        print(num1-num2)    
    case "c":
        print(num1*num2)
    case "d":
        print(num1/num2)  