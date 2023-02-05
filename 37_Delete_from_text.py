# Напишите программу, удаляющую из текста все слова, содержащте "абв"

orig_text = 'Питон - наабвверное самый лучший из хуабвдших языков!'
orig_list =[]
for i in orig_text.split():
    if not 'абв' in i:
        orig_list.append(i)
print(' '.join(orig_list))  

#или
print(' '.join(list(filter(lambda x: not 'абв' in x, orig_text.split()))))