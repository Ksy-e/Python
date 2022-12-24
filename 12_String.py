#Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другую.

text = 'Напишите программу, в которой пользователь будет задавать две строки'
search = input('Введите искомый текст: ')
print(text)
text=text.split()
count=0
print(text)
for word in text:
    if search in word:
        count += 1

print(f'В заданном тексте подстрока {search} встерчается {count} раз')

text = 'Напишите программу, в которой пользователь будет задавать две строки'
print(text)
search = input('Введите искомую букву: ')
count=0
for word in text:
    for char in word:
        if search == char:
            count += 1

print(f'В заданном тексте подстрока {search} встерчается {count} раз')

#или

text = 'Напишите программу, в которой пользователь будет задавать две строки'
search = input('Введите искомый текст: ')
text=text.split(search)
print(text)
print(len(text)-1)