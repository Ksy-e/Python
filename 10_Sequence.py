# Напишите программу, которая принимает на вход число N и выдаёт последовательность из
#  N членов.Пример:
# - Для N = 5: 1, -3, 9, -27, 81

N= int(input('Введите число: '))
for i in range(N):
    print(str(f'{(-3)**i}'),end=" ")
#или
N= int(input('Введите число: '))
result=[]
for i in range(N):
    result.append((-3)**i)
    print(f'Для N = {N}:', end=' ')
    print(*result, sep=', ')
