list1= [1,2,5,4,6,8,9]
list2 =[]
menor_posible=5555
menor_posicion=0
i=0
for i in range(len(list1)):
    menor_posible = 0
    for j in range(len(list1)-1):
        if menor_posible > list1[j+1]:
            menor_posible=list1[j+1]
            menor_posicion=j+1
    list2.append(menor_posible)
    if len(list1) != 1:
        list1.pop(menor_posicion)

print(list1)
print(list2)