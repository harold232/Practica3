class Alumno:
    pass
    def Display(self, nombre, numeroReg):
        print(f"Nombre del alumno: {nombre}")
        print(f"Numero de registro: {numeroReg}")
    
    def setAge(self, edad):
        print(f"Edad del alumno: {edad}")

    def setNota(self, nota1, nota2):
        print("Nota del alumno {} - {}".format(nota1, nota2))

alumno1 = Alumno()
alumno1.nombre = "Harold"
alumno1.numeroReg = "0244"
alumno1.edad = "20"
alumno1.nota1 = "16"
alumno1.nota2 = "13"
alumno1.Display(alumno1.nombre, alumno1.numeroReg)
alumno1.setAge(alumno1.edad)
alumno1.setNota(alumno1.nota1, alumno1.nota2)

