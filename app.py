# Clase Alumno
class Alumno:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def presentarse(self):
        print(f"Soy {self.nombre} y estudio {self.carrera}")

alumno1 = Alumno("Anacleto", "Entornos")
alumno1.presentarse()
alumno2 = Alumno("Filomena", "Entornos")
alumno2.presentarse()
alumno3 = Alumno("Alejandro", "Entornos")
alumno3.presentarse()