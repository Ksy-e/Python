
list1 = [1,2,3,4,5]
list2=list1
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

list1[0] = 123 #значение изменится в обоих списках
list2[1]=333 #значение измениться в обоих списках
print(list1.pop(2)) #удалит второй элемент из списка
print(list1.insert(2,11)) #добавит на второй элемент 11
print(list1.append(11)) #добавит 11 в конец списка
