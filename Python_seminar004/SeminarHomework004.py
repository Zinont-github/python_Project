# # 30
# N = float(input())
# d = float(input())
# count = 0
# while d != 1:
#     d *= 10
#     count += 1
#
# print(round(N, count))
#

# 31

# N = int(input())
# n = N
# i = 2
# numbers = []
#
# while i < N:
#     while N % i == 0:
#         N = int(N / i)
#         numbers.append(i)
#     i += 1
# if N == i:
#     numbers.append(i)
# if len(numbers) == 1:
#     numbers.append(n)
#     print("Number easy")
#     exit()
# print(n, end=' = ')
# print(*numbers, sep=' * ')

# 32

# numbers = list(map(int, input().split()))
# new_numbers = []
# for i in range(len(numbers)):
#     if numbers[i] not in new_numbers:
#         new_numbers.append(numbers[i])
# print(new_numbers)

# 34

from random import randint
from sympy import symbols
from math import prod

max_val = 100
k = int(input('Введите натуральную степень k:'))
list = [randint(1, max_val) for i in range(k + 1)]
x = symbols('x')
n = (sum(map(prod, zip(list, [x ** i for i in range(k + 1)]))))
with open('text.txt', 'w') as data:
    data.write(str(n))
