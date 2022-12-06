'''2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''
numbers = list(map(int, input("Введите числа через пробел: ").split()))
def Product(numbers):
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
Product(numbers)