#В файле хранятся числа, нужно выбрать четные и составить список пар (число,
#  квадрат числа)

path = '/Users/KSY/Desktop/Домашнее задание/Python/36_File.txt'
f = open(path, 'r')
data = f.read()+' '
f.close()
numbers = []
print(numbers)
while data !=' ':
    space_pos=data.index(' ')
    numbers.append(int(data[:space_pos]))
    data=data[space_pos+1:]
out = []
for e in numbers:
    if not e%2:
        out.append(e,e**2)
print(out)