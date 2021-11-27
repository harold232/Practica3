def trianguloPascal(filas):
    print(' '*filas, 1)
    for i in range(1, filas):
        res = 11 ** i
        print(f"{' '*(filas - i + 1)}{res}")
        
filas = int(input("Ingrese el numero de filas de la piramide: "))
trianguloPascal(filas)