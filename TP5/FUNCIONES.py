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
     resultado = x1 / x2
     return resultado
    
def solicitar_datos():
    while True:
        try:
            x1 = float(input("ingrese un numero aqui: "))
            x2 = float(input("ingrese un segundo numero aqui: "))
            break
        except Exception as ex:
            print("No se pueden usar letras, ", TypeError(ex))
    return x1,x2

def solicitar_datos_ans():
    while True:
        try:
            x2 = float(input("ingrese un segundo numero aqui: "))
            break
        except Exception as ex:
            print("No se pueden usar letras, ", TypeError(ex))
    return x2
