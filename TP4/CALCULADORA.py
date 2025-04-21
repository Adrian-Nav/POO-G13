while True:
    print("1-suma")
    print("2-resta")
    print("3-multiplicacion")
    print("4-division")
    print("5-ninguna")
    c = int(input("ingrese una suma, resta, multiplicacion o division: "))

    if c ==5:
        print("OFF")
        break

    if c ==1:
         a = int(input("ingrese un numero: "))
         b = int(input("ingrese otro numero: "))
         print("El resultado de la suma es ",a+b)
    elif c ==2:
         a = int(input("ingrese un numero: "))
         b = int(input("ingrese otro numero: "))
         print("El resultado de la resta es ",a-b)
    elif c ==3:
         a = int(input("ingrese un numero: "))
         b = int(input("ingrese otro numero: "))
         print("El resultado de la multiplicacion es ",a*b)
    elif c ==4:
         a = int(input("ingrese un numero: "))
         b = int(input("ingrese otro numero: "))
         print("El resultado de la division es ",a/b)
    else:
        print("le pifiaste")

    
    


