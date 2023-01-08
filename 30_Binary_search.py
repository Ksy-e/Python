#Бинарный поиск
#В переменных low и high хранятся границы той части списка, в которой выполняется поиск

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high: # Пока эта часть не скоратиться до одного элемента
        mid = (low+high) # проверяем средний элемент
        guess = list[mid]
        if guess == item: # значение найдено
            return mid
        if guess > mid-1: # много
            high = mid-1
        else:             # мало
            low = mid+1
    return None           # значение не существует

my_list = [1,3,5,7,9]
print(binary_search(my_list,3))
print(binary_search(my_list,-1))