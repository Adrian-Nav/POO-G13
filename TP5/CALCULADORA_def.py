import FUNCIONES as f
flag=False
ans = None
while True:
    a = float(input("solicite la operacion que quiere realizar: "))
    if flag:
        x1=ans

    if a ==5:
       print("OFF")
       break

    if a ==1:
        a,b=f.solicitar_datos()
        rs=f.suma(a,b)
        print(rs)

    elif a ==2:
        a,b=f.solicitar_datos()
        rs=f.resta(a,b)
        print(rs)

    elif a ==3:
        a,b=f.solicitar_datos()
        rs=f.mult(a,b)       
        print(rs)

    elif a ==4:
        a,b=f.solicitar_datos()
        rs=f.div(a,b)
        print(rs)

    elif a ==6:    
        ans ==None
        continue

    else:
        print("cualquiera master")
    ans=rs
    flag= True