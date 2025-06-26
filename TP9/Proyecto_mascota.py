class Mascota:   
     def __init__(self, nombre, especie):
          self.nombre = nombre
          self.especie = especie
          self.energia=80
          self.felicidad=70
          self.hambre=60

     def limitar_valores(self):
          self.energia = max(0,min(100,self.energia))
          self.felicidad = max(0,min(100,self.felicidad))
          self.hambre = max(0,min(100,self.hambre))

     def jugar(self):
          self.felicidad=+20
          self.energia=-30
          self.hambre=+20
          print("Que perro revoltoso")

     def comer(self):
          self.felicidad=+10
          self.energia=+20
          self.hambre=-60          
          print("Cuanta hambre tenia")

     def dormir(self):
          self.felicidad=+10
          self.energia=+60
          self.hambre=+50          
          print("Parece un ladrillo")

nombre = input("Como se llama tu mascota: ")
especie = input("Que especie es tu mascota: ")
a = input("Que quieres que haga tu mascota: ")

mascota1 = Mascota(nombre, especie)

mascota1.jugar()
mascota1.comer()
mascota1.dormir()