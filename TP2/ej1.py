list1= [1,2,5,4,6,8,9]
list2 =[]
j=0
i=0
d=0
if i < 7 and j < 7:
    for j in range(len(list1)) :
        for i in range(1,len(list1)-1):
            if list1[j] < list1[i] :
                d = list1[j]
        list2.append(d) 
        list1.pop(j) 
print(list2) 