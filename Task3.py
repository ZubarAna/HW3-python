'''3.Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
list1 = list(map(float, input("Введите числа через пробел: ").split()))
list2 = []
for i in list1:
    if i % 1 != 0:
        list2.append(round(i % 1, 2))
print(list2)
max = list2[0]
for i in range(len(list2)):
    if list2[i] > max:
        max = list2[i]
print(f'Максимальное значение дробной части элементов - {max}')
min = list2[0]
for i in range(len(list2)):
    if list2[i] < min:
        min = list2[i]
print(f'Минимальное значение дробной части элементов - {min}')

print(f'Разница между максимальным и минимальным значением дробной части элементов - {max - min}')
