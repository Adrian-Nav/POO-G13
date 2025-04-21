f=69
g=0
d = int(input("adivina pa, vos podes: "))
while g < 7:
    if d < 69:
        print("Te quedaste corto")
    elif d > 69:
        print("Te pasaste")
    elif d == f:
        print("Ganaste")
    elif d > f or d < f:
        g = g+1


