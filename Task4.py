'''4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
num10 = int(input('Введите число: '))
num2 = ''
while num10 != 0:
    num2 += str(num10 % 2)
    num10 //= 2
print(num2[::-1])