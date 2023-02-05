#Дан список чисел. Создайте список, в котрый попадают числа, описывающие возрастающую 
#последовательность. Порядок элементов менять нельзя.

import random

my_list = [i for i in range(20)]
random.shuffle(my_list)
new_list=[]
for i in range(len(my_list)):
    current = my_list[i]
    sub_list = [current]
    for k in range(i+1, len(my_list)-1):
        if current + 1 == my_list[k]:
            sub_list.append(my_list[k])
            current+=1
    if len(sub_list)>=2:
        new_list.append(sub_list)
print(my_list)
print(new_list)