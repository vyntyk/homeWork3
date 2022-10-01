# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5
k = int(input('Введите число: '))


def get_fibonacci(n):
    fib_numbers = []
    a, b = 1, 1
    for i in range(n):
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers


fib_norm = get_fibonacci(k)
fib_neg = list(reversed(fib_norm))
for i in range(len(fib_neg)):
    if k % 2 == 0:
        if i % 2 == 0:
            fib_neg[i] *= -1
    else:
        if i % 2 != 0:
            fib_neg[i] *= -1
fib_neg.append(0)
print(f'Для k = {k} список чисел:', fib_neg + fib_norm)
