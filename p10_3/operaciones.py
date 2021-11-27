def Suma(num1, num2):
    suma = num1 + num2
    return suma

def Resta(num1, num2):
    resta = num1 - num2
    return resta

def Multiplicacion(num1, num2):
    mult = num1 * num2
    return mult

def Division(num1, num2):
    while True:
        try:    
            div = num1 / num2
            return div
            break 
        except:
            return "No es posible dividir entre cero."
            break


