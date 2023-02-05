#В файле находится N натуральных чисел, записаннх через пробел.Среди них не хватате одного,
#что бы выполнялось условие A[i]-1=A[i-1]. Найдите это число.

new_str = '1,2,3,5,6'
new_list=new_str.split(',')
a=1
for i in range(len(new_list)):
    new_list[i]=int(new_list[i])
    if new_list[i]!=i+1:
        print(new_list[i]-1)
        break