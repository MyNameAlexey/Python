# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент(a1), разность(d) 
# и количество элементов(n) нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

n = int(input('Input n ')) #общее кол-во эл-в
x = int(input('Input a[0] '))
d = int(input('Input d ')) #шаг
print(*range(x, x + d * n, d))