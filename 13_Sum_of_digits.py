# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр. Пример: 6782 -> 23 0,56 -> 11

num = input('Введите число: ')
sum = 0
for digit in num:
    if digit.isdigit():
        sum += int(digit)
print(f'Сумма цифр числа {num} равна {sum}')