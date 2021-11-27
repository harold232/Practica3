class Rectangulo:
    pass
    def area(self, largo, ancho):
        a = largo * ancho
        print(a)

rect = Rectangulo()
largo = float(input("Ingrese el largo del rectangulo: "))
ancho = float(input("Ingrese el ancho del rectangulo: "))
print("El area del rectangulo es: ", end = ' ')
rect.area(largo, ancho)