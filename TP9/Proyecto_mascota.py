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
          self.felicidad+=20
          self.energia-=30
          self.hambre+=20
          print(f"Que perro revoltoso,felicidad={self.felicidad},energia=¨{self.energia},hambre={self.hambre}")

     def comer(self):
          self.felicidad+=10
          self.energia+=20
          self.hambre-=60          
          print(f"Cuanta hambre tenia,felicidad={self.felicidad},energia=¨{self.energia},hambre={self.hambre}")

     def dormir(self):
          self.felicidad+=10
          self.energia+=60
          self.hambre+=50          
          print(f"Parece un ladrillo,felicidad={self.felicidad},energia=¨{self.energia},hambre={self.hambre}")

nombre = input("Como se llama tu mascota: ")
especie = input("Que especie es tu mascota: ")
mascota1=Mascota(nombre,especie)

while True:
     a = input("Que quieres que haga tu mascota: ")

     if a=="jugar":
          mascota1.jugar()
     elif a=="dormir":
          mascota1.dormir()
     elif a=="comer":
          mascota1.comer()




