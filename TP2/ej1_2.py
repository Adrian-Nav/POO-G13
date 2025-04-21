list1 = [2, 7, 4, 6, 9, 8, 1, 5, 3]
list2 = []
for i in range(len(list1)):
    menor_posible = 99999
    menor_posicion = -1
    for j in range(len(list1)):
        if list1[j] < menor_posible:
            menor_posible = list1[j]
            b = j

    list2.append(menor_posible)
    list1[b] = 99999
print(list2)