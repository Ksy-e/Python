#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
#  максимум использование библиотеки Random для и получения случайного int
from random import randint as RI
my_list=[]
for i in range(10):
    my_list.append(RI(0,100))
print(f'Изначальный список: {my_list}')

for i in range(len(my_list)-1, 0, -1):
    j = RI(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(f'Перемешанный список: {my_list}')

#с использованием ускоренной обработки даных

my_list1=[RI(0,100) for i in range(10)]
print(f'Изначальный список: {my_list1}')

def suff(my_list1):
    for i in range(len(my_list1)-1, 0, -1):
        j = RI(0, i + 1)
        my_list1[i], my_list1[j] = my_list1[j], my_list1[i]

my_list2=list(filter(suff(my_list1), my_list1))
print(f'Перемешанный список: {my_list2}')
