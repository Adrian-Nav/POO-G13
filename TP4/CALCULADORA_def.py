def suma(x1, x2):
    resultado = x1 + x2
    return resultado
    
def resta(x1, x2):
    resultado = x1 - x2
    return resultado

def mult(x1, x2):
    resultado = x1 * x2
    return resultado

def div(x1, x2):
    if x2 ==0:
        print("no se puede pa")
    else:
        resultado = x1 / x2
        return resultado

def solicitar_datos():
    x1 = float(input("ingrese un numero aqui: "))
    x2 = float(input("ingrese un segundo numero aqui: "))
    return x1,x2



while True:
    a = float(input("solicite la operacion que quiere realizar: "))
    if a ==5:
       print("OFF")
       break

    if a ==1:
        a,b=solicitar_datos()
        rs= suma(a,b)
        print(rs)

    elif a ==2:
        a,b=solicitar_datos()
        rs= resta(a,b)
        print(rs)

    elif a ==3:
        a,b=solicitar_datos()
        rs= mult(a,b)       
        print(rs)
    elif a ==4:
        a,b=solicitar_datos()
        rs= div(a,b)
        print(rs)
    
    else:
        print("cualquiera master")