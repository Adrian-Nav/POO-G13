class Perro:

    especie ="mamifero"

    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        self.nombre = nombre
        self.raza = raza

mi_perro = Perro("Choc", "Mestizo")
print(type(mi_perro))
print(Perro.especie)