def solicitar_datos():
    a = float(input("ingrese numero a aqui: "))
    b = float(input("ingrese numero b aqui: "))
    c = float(input("ingrese numero c aqui: "))
    return a,b,c

def vertice(a,b,c):
    x = -(b)/2*(a)
    y = a*x**2+b*x+c
    return x,y