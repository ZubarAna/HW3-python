'''1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
from random import random, randint
N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers)
SumOfElements = 0
for elements in range(len(numbers)):
    if elements % 2 != 0:
        SumOfElements += numbers[elements]
        print(SumOfElements)
print()
print(f'Сумма элементов на нечетной позиции равна {SumOfElements}')