#Напишите программу, которая принимает на вход дробное число, и показывает
#первую цифру после запятой. 6,78->7, 5->нет, 0,34->3

number=float(input('Введите число: '))
ost=(number*10)%10
if number-round(number)==0:
    print('Нет')
else:
    print(round(ost))

# или
num=float(input('Введите число: '))
print(int(num*10)%10)

# или

my_str=input('Введите число: ')
i=0
for el in my_str:
    if el=='.' or el==',':
        print(my_str)
    i+=1
# или
numm=input('Введите число: ')
numm.split('.')
if len(numm)<2:
    print('целое')
else:
    print(numm[1][0])