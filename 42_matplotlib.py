import numpy as np
import matplotlib.pyplot as plt

a, b, c = 5, 10, -30

def func(x):
    return a*x**2 + b*x + c

limit = 5
step = 0.01

x = np.arange(-limit,limit,step)

def take_roots(a,b,c) ->tuple:
  discr = (b**2 - 4*a*c)
  if discr > 0:
    x1 = (-b + discr**0.5)/(2*a)
    x2 = (-b - discr**0.5)/(2*a)
    return round(x1,2), round(x2,2)
  elif discr == 0:
    x = -b/(2*a)
    return (round(x,2), )
  else:
    return (None, )

roots = take_roots(a,b,c)
print(roots)

min_y = min(func(x))
min_x = take_roots(a,b,c-min_y)[0]
print(min_x, min_y)

x_down_pos = np.arange(-limit, min(roots)+step, step)
x_down_neg = np.arange(min(roots), min_x+step, step)
x_up_neg = np.arange(min_x,max(roots)+step, step)
x_up_pos = np.arange(max(roots),limit+step, step)

plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_down_pos, func(x_down_pos), 'b', label = 'Убываение больше 0')
plt.plot(x_up_pos, func(x_up_pos), 'r', label = 'Возрастание больше 0')

plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x_down_neg, func(x_down_neg), 'b', label = 'Убываение меньше 0')
plt.plot(x_up_neg, func(x_up_neg), 'r', label = 'Возрастание меньше 0')

if len(roots)==2:
  plt.plot(roots[0], 0, 'yo', label = f'Корни ({roots[0]}, {roots[1]})')
  plt.plot(roots[1], 0, 'yo')
else:
  if roots[0] != None:
    plt.plot(roots[0], 0, 'yo', label = f'Корни ({roots[0]}, {roots[1]})')
plt.plot(min_x, min_y, 'gx', label = f'Экстремум функции ({min_x}, {min_y})')
plt.legend()
plt.grid()
plt.show()


