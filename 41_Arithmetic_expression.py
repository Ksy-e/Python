#Напишите программу вычисления арифметического выражения, заданного строкой.
# Используйте операции +,-,/,*. Приоритет операций стандартный.
#2+2=>4  1+2*3=>7   1-2*3=5

#ex = '2-3*4-10-/2'
#ex = ex.replace(' ', '')
#ex = ex.replace('+', ' + ').replace('-', ' - ').replace('*' ,' * ').replace('/', ' / ')
#ex = ex.split()
#print(ex)
#while len(ex)>1:
    #i=0
    #while '*' in ex or '/' in ex:
        #if ex[i] == '*':
            #ex[i-1]=int(ex[i-1]) * int(ex[i+1])
           #ex.pop(i)
           # ex.pop(i)
        #elif ex[i] == '/':
            #ex[i-1]=int(ex[i-1]) / int(ex[i+1])
            #ex.pop(i)
            #ex.pop(i)
        #else:
            #i+=1
    #i=0
    #while '+' in ex or '-' in ex:
        #if ex[i] == '+':
            #ex[i-1]=int(ex[i-1])+int(ex[i+1])
            #ex.pop(i)
            #ex.pop(i)
        #elif ex[i] == '-':
            #ex[i-1]=int(ex[i-1])-int(ex[i+1])
            #ex.pop(i)
           # ex.pop(i)
        #else:
          #  i+=1

#print(ex)

str = '(1+2)*3-1+2*3'
print(str, ' = ', eval(str), '\n')

data = '1 - 2* 3'
temp_data = data.replace(' ', '')
temp_data = data.replace('+', ' + ').replace('-',
' - ').replace('*', ' * ').replace('/', ' / ').split()
print(temp_data)

for operation in ['*','/','-','+']:
    while operation in temp_data:
        index = temp_data.index(operation)
    if operation == '*':
        temp_data[index-1] = int(temp_data[index-1]) * int(temp_data.pop(index+1))
    elif operation == '/':
        temp_data[index-1] = int(temp_data[index-1]) / int(temp_data.pop(index+1))
    elif operation == '-':
        temp_data[index-1] = int(temp_data[index-1]) - int(temp_data.pop(index+1))
    elif operation == '+':
        temp_data[index-1] = int(temp_data[index-1]) + int(temp_data.pop(index+1))
    temp_data.pop(index)
    break
print(temp_data)