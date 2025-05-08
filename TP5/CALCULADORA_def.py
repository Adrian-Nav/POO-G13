import FUNCIONES as f

flag=False
ans = None

while True:
    a = float(input("solicite la operacion que quiere realizar: "))
    d= input("quiere usar el resultado anterior?(s/n): ")

    if d=="s":
        flag=True
    elif d=="n":
        flag=False

    if a ==5:
       print("OFF")
       break

    if a ==1:
        if flag:
            a=ans
            b=float(input("ingrese un segundo numero aqui: "))
        else:
            a,b=f.solicitar_datos()
        rs=f.suma(a,b)
        print(rs)

    elif a ==2:
        if flag:
            a=ans
            b=float(input("ingrese un segundo numero aqui: "))
        else:
            a,b=f.solicitar_datos()
        rs=f.resta(a,b)
        print(rs)
    elif a ==3:
        if flag:
            a=ans
            b=float(input("ingrese un segundo numero aqui: "))
        else:
            a,b=f.solicitar_datos()
        rs=f.mult(a,b)
        print(rs)

    elif a ==4:
        if flag:
            a=ans
            b=float(input("ingrese un segundo numero aqui: "))
        else:
            a,b=f.solicitar_datos()
        rs=f.div(a,b)
        print(rs)

    else:
        print("cualquiera master")
    ans=rs
    flag= True