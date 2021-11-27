while True:
    try:
        calificaciones = str(input("Ingrese una lista de calificaciones separadas por coma: "))
        lista = []
        for i in calificaciones.split(','):
            num = int(i)
            lista.append(num)
        print(lista)
    except:
        print("Los valores introducidos no pueden ser convertidos debido a un error de tipeo")
