# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def pow_recurcive(n, m):
    if m == 1: # Место остановки
        return n
    elif m % 2 == 0: # для чётного случая
        res = pow_recurcive(n, m // 2)
        return res * res
    else: # для нечётного случая
        res = pow_recurcive(n, m // 2)
        return res * res * n
n, m = int(input()), int(input())
print(pow_recurcive(n, m))