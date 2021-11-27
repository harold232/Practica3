import random

def lista():
    num = [ ]
    for i in range(0, 20):
        al = random.randint(1,100)
        num.append(al)
    return num    

def mostrar(num):
    print(num)

def ordenar(num):
    num.sort()
    mostrar(num)
        


