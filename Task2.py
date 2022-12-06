'''2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''
from random import random, randint
N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers)
prod = 0
lenght = 0
result = []
if len(numbers) % 2 != 0:
    lenght = len(numbers) // 2 + 1
else:
    lenght = len(numbers) // 2
for i in range(lenght):
    prod = numbers[i] * numbers[len(numbers) - i - 1]
    result.append(prod)
print(result)