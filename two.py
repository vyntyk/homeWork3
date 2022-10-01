# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10]
# [20, 40]#
# in 5 out [2, 2, 4, 8, 8]
# [16, 16, 4]

import random

spisok = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    spisok.append(random.randint(1, 10))
print(f"Cписок:\n {spisok}")
sumNum = 0
len_list = 0
if len(spisok) % 2 == 0:
    len_list = len(spisok) // 2
    for i in range(len_list):
        print(spisok[i] * spisok[len(spisok) - 1 - i], end=" ")

else:
    len_list = len(spisok) // 2
    for i in range(len_list):
        print(spisok[i] * spisok[len(spisok) - 1 - i], end=" ")

    print((spisok[len(spisok) // 2]))
