import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")




my_str='3*x**2 - 12*x + 6 = 0'

def cut(string: str):
    eq=[]
    string = string.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split()
    for item in string:
        eq.append(item.split('*x')[0])
    return eq

a, b, c = cut(my_str)

print(a)
print(b)
print(c)