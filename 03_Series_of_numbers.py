#Напиишите программу, которая будет на вход приимать число n и выводить
# числа от -n до n
# 3->-3, -2, -1, 0, 1, 2, 3

n=int(input('Введите число: '))
my_str=''
for i in range(-n,n+1):
    my_str+=str(i)+', '
print(my_str[:-2])