import random
def numero_al():
    num_al = random.randint(1, 100)
    return num_al

def pedir():
    n = int(input("Ingrese un numero: "))
    return n

def adivinar(num_al):
    num = pedir()
    while num != num_al:
        if num > num_al:
            print("Ingrese un numero inferior")
            num = pedir()
        elif num < num_al:
            print("Ingrese un numero superior")
            num = pedir()
    if num == num_al:
        print("Has ganado")

