class Alumno:
    def __init__(self, nombre, carrer):
        self.nombre = nombre
        self.carrera = carrera

    def presentarse(self):
        print(f"Soy {self.nombre} y estudio {self.carrera}")

alumno1 = Alumno("Anacleto", "Entornos")
alumno1.presentarse()