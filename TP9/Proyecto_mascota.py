class Mascota:   
     def __init__(self, nombre, especie):
          self.nombre = nombre
          self.especie = especie
          self.energia=80
          self.felicidad=70
          self.hambre=60
          self.aura=0

     def limitar_valores(self):
          self.energia = max(0,min(100,self.energia))
          self.felicidad = max(0,min(100,self.felicidad))
          self.hambre = max(0,min(100,self.hambre))

     def jugar(self):
          self.felicidad+=20
          self.energia-=30
          self.hambre+=20
          self.limitar_valores()
          print(f"Que perro revoltoso")
          print(f"felicidad={self.felicidad},energia={self.energia},hambre={self.hambre}")

     def comer(self):
          self.felicidad+=10
          self.energia+=20
          self.hambre-=60   
          self.limitar_valores()       
          print(f"Cuanta hambre tenia.")
          print(f"felicidad={self.felicidad},energia={self.energia},hambre={self.hambre}")

     def dormir(self):
          self.felicidad+=10
          self.energia+=60
          self.hambre+=50   
          self.limitar_valores()       
          print(f"Parece un ladrillo. ")
          print(f"felicidad={self.felicidad},energia={self.energia},hambre={self.hambre}")

     def backflip(self):
          self.aura+=1000000
          self.felicidad+=10000
          self.energia-=100
          self.hambre+=100
          print("No lo puedo creer, CUANTA AURA.")
          print(f"aura={self.aura},felicidad={self.felicidad},energia={self.energia},hambre={self.hambre}")

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
     elif a=="backflip":
          mascota1.backflip()
     elif a=="nada":
          break




