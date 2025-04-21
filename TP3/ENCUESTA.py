a=[]
c=0
for i in range (1, 6):
    b = int(input("ingrese una edad"))
    while b<0  :
        print("el numero es negativo, intente de nuevo")
        b = input("ingrese una edad")
        b>0 
        print("el numero es positivo")
    a.append(b)
print(a)
for i in range (0,5):
    if a[i] < 18:
        print("son menores de edad")
    elif a[i] > 18 and a[i] < 65:
        print("son adultos")
    elif a[i] > 65:
        print("son viejardos")