# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.(положительные числа)

str = '267 12 963'
list1 = str.split()
max = int(list1[0])
min = int(list1[0])
for i in list1:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print('min = ', min, '; max = ', max)

