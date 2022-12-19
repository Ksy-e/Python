#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
#1,4,8,7,5-8; 78,55,36,90,2-90

number1=int(input('Введите первое число: '))
number2=int(input('Введите второе число: '))
number3=int(input('Введите третье число: '))
number4=int(input('Введите четвертое число: '))
number5=int(input('Введите пятое число: '))
max=number1
if number2>max:
    max=number2
    if number3>max:
        max=number3
        if number4>max:
            max=number4
            if number5>max:
                max=number5
print(max)

#другой вариант решения

list=[0,0,0,0,0]
for i in range(len(list)):
    list[i]=int(input('Введите число: '))
    print(list)
    maxx = list[0]
    for i in range(len(list)):
        if maxx<list[i]:
            maxx=list[i]
print(maxx)