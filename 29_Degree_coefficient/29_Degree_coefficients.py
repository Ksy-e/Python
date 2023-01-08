#A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#B. Даны два файла, в каждом из которых находится запись многочлена. Задача - 
# сформировать файл, содержащий сумму многочленов.
#НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
#Расширить значение коэффициентов до [-100..100]

import random

def create_eq():
    eq = {}
    n = int(input("Введите натуральную степень k = "))
    for i in range(n,-1,-1):
        if i == n:
            while True:
                koef = random.randint(0,100)
                if koef != 0:
                    break
            eq[i] = koef
        else:
            eq[i]=random.randint(0,100)
    return eq

eq1 = create_eq()
eq2 = create_eq()
print(eq1)
print(eq2)
one = dict.values(eq1)
two = dict.values(eq2)

eq3 = [x+y for x, y in zip(one, two)]
print(eq3)
eq3.reverse()


def create_str (eq1):
    lst = eq1
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


def write_file (name, eq1):
     with open(name, 'w') as data:
         data.write(eq1)

write_file("file1.txt", create_str(eq1))
write_file("file2.txt", create_str(eq2))
write_file("file3.txt", create_str(eq3))

one = create_str(eq1)
two = create_str(eq2)
three = create_str(eq3)

print(f'Первый многочлен: {one}')
print(f'Второй многочлен: {two}')

print(f'Результат сложения {three}')
