# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in  5 out [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in 3 out [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
import random

list = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    list.append(round(float(random.random() * 100), 2))
print(f"Cписок: \n {list}")

def find_different(any_numbers):
    numbers = [round(x - int(x), 2) for x in (any_numbers)]
    numbers = [x for x in numbers if type(x) == float]
    return max(numbers) - min(numbers)


print('Разница = >', find_different(list))
