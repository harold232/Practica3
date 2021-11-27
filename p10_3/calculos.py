from operaciones import *

try: 
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    suma = Suma(num1, num2)
    resta = Resta(num1, num2)
    mult = Multiplicacion(num1, num2)
    div = Division(num1, num2)
    print(f"La suma es: {suma}")
    print(f"la resta es: {resta}")
    print(f"La multiplicacion es: {mult}")
    print(f"La divison es: {div}")
except:
    print("Tipo de dato no válido.")