vocales = ["a","e","i","o","u"]
v=0
a= input("ingrese una palabra o una frase: ")
while a==" ":
    a= input("ingrese una palabra o una frase: ")

for i in a :
    if i in vocales :
        v=v+1
print(v) 
if v >= 5:
    print("Mucho contenido vocal")
    a= input("ingrese una palabra o una frase: ")