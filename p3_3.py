class Circulo:
    pass
    def area(self, radio):
        a = 3.1415 * radio * radio
        print(a)

circ1 = Circulo()
radio = float(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ", end = ' ')
circ1.area(radio)