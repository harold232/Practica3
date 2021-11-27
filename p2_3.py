def mayus(): 
    cadena = str(input("Ingrese una oracion: "))
    cadena2 = ''
    for i in cadena.split():
        cadena2 += i[0].upper() + i[1:] + ' '
    return cadena2

cadena2 = mayus()
print(cadena2)