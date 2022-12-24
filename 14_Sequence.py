#Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример: Для n=4 -> [2, 2.25, 2.37, 2.44] Сумма 9.06

N= int(input('Введите число: '))
result=[]
for i in range(1,N+1):
    result.append((1+1/i)**i)
sum =0
for digit in result:
    sum+=digit
print(f'Для N = {N}:', end=' ')
print(result, sep=', ', end=' ')
print(f'Сумма = {round(sum,2)}')