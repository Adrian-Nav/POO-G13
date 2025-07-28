import metodos as m

try:
     nombre = input("Como se llama tu mascota: ")
     especie = input("Que especie es tu mascota: ")
     mascota1=m.Mascota(nombre,especie)
except ValueError:
     print("Escriba algo válido")
     
while True:
     try:
          a = input("Que quieres que haga tu mascota: ")
     except ValueError:
          print("Escriba algo válido")
          continue
     
     if a=="jugar":
          mascota1.jugar()
     elif a=="dormir":
          mascota1.dormir()
     elif a=="comer":
          mascota1.comer()
     elif a=="backflip":
          mascota1.backflip()
     elif a=="volar":
          mascota1.volar()
     elif a=="nada":
          break
     else:
          print("Cualquiera bro")





