import FUNCIONES as f

flag=False
ans = None

while True:
    try:
        a = float(input("solicite la operacion que quiere realizar: "))
    except ValueError:
        print("Escriba un numero valido: ")
        continue

    if a ==5:
       print("OFF")
       break
    
    try:
        d= input("quiere usar el resultado anterior?(s/n): ")
        if d=="s":
            x=ans+1
    except Exception as ex:
        print("no hay valor de ans, el error es: ", TypeError(ex))
        d="n"

    if d=="s":
            flag=True
    elif d=="n":
            flag=False

    if a ==1:
        if flag:
            a=ans
            b=f.solicitar_datos_ans()
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
        try:
            if flag:
                a=ans
                b=float(input("ingrese un segundo numero aqui: "))
            else:
                a,b=f.solicitar_datos()
            rs=f.div(a,b)
            print(rs)
        except ZeroDivisionError:
            print("No se puede dividir un numero por 0")
            continue
        
    else:
        print("cualquiera master")