class Mascota:   
     def __init__(self, nombre, especie):
          self.nombre = nombre
          self.especie = especie
          self.energia=80
          self.felicidad=70
          self.hambre=60
          self.aura=0
          self.altitud=0

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
          print(f"felicidad={self.felicidad}%,energia={self.energia}%,hambre={self.hambre}%")

     def comer(self):
          self.felicidad+=10
          self.energia+=20
          self.hambre-=60   
          self.limitar_valores()       
          print(f"Cuanta hambre tenia.")
          print(f"felicidad={self.felicidad}%,energia={self.energia}%,hambre={self.hambre}%")

     def dormir(self):
          self.felicidad+=10
          self.energia+=60
          self.hambre+=50   
          self.limitar_valores()       
          print(f"Parece un ladrillo. ")
          print(f"felicidad={self.felicidad}%,energia={self.energia}%,hambre={self.hambre}%")

     def backflip(self):
          self.aura+=1000000
          self.felicidad+=10000
          self.energia-=100
          self.hambre+=100
          self.limitar_valores()
          print("No lo puedo creer, CUANTA AURA.")
          print(f"aura={self.aura}%,felicidad={self.felicidad}%,energia={self.energia}%,hambre={self.hambre}%")

     def volar(self):
          self.aura+=102120120
          self.felicidad+=12334234
          self.energia-=80
          self.hambre+=30
          self.altitud+=1000000
          self.limitar_valores()
          print("aura, una mascota que vuela")
          print(f"aura={self.aura}%,felicidad={self.felicidad}%,energia={self.energia}%,hambre={self.hambre}%,altitud={self.altitud}m")
