#Напишите программу, которая по заданному номеру четверти, показывает диапазон 
#возможных координат точек в этой четверти (x и y).
q= int(input('Введите номер четверти '))

if(q==1):
   print('x>0 и y>0')
else:
   if (q==2):
      print('x>0 и y<0')
   else:
      if (q==3):
         print('x<0 и y<0')
      else:
         if (q==4):
            print('x<0 и y>0')