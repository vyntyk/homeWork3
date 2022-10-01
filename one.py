# #1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in 5 out [10, 2, 3, 8, 9]# 22
# in 4 out [4, 2, 4, 9] # 8

import random

spisok = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    spisok.append(random.randint(1, 20))
print(f"Cписок: \n {spisok}")
sumNum = 0

for i in range(0, len(spisok), 2):
    sumNum += spisok[i]
print(f'Сумма чисел на нечетных позициях: {sumNum}')
