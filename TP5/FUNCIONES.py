import CALCULADORA_def as c

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
