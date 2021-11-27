def longitud():
    n = 0
    cadena = str(input("Ingrese una oracion: "))
    for i in cadena:
        if i != ' ':
            n += 1
        else:
            n = 0
    return n

long = longitud()
print(f"La longitud de la ultima palabra es: {long}")