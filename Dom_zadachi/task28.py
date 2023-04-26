# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

# *Пример:*

# 2 2
#     4

def sum_arr(arr, size):
    if (size == 0):
        return 0
    else:
        return arr[size - 1] + sum_arr(arr, size - 1)
n = int(input('Введите длину списка: '))
a = []
for i in range(0, n):
    element = int(input('Введите элемент списка: '))
    a.append(element)
print("Весь список:")
print(a)
print("Сумма элементов списка равна:")
b = sum_arr(a, n)
print(b)
