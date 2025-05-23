import func as d
import matplotlib.pyplot as plt

a,b,c = d.solicitar_datos()
x_v,y_v = d.vertice(a,b,c)

x = []
y = []
inicio = -10
fin = 10
paso = (fin - inicio) / 399
for i in range(400):
    valor_x = inicio + i * paso
    x.append(valor_x)
    y.append(a * valor_x**2 + b * valor_x + c)

print("y del vertice es: ",(y_v))
print("x del vertice es: ",(x_v))

plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
plt.title('Función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()