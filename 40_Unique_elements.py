#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#[1,2,3,5,1,5,3,10] =>[2,10]

my_list = [1,2,3,5,1,5,3,10]
nums = list(filter(lambda x: my_list.count(x)==1,my_list))
print(nums)
