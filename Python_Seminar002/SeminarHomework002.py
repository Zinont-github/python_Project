# 14

# n = int(input('Введите число: '))
# sum = 0
# while n > 0:
#     plus = n % 10
#     sum += plus
#     n = n // 10
# print(sum)

# 15
# n = int(input())
# i = 1
# sum = 1
# print(end='(')
# while i <= n:
#     if i == n:
#         print(n * sum, end=')')
#     else:
#         sum *= i
#         print(sum, end=',')
#     i += 1
# 16 1-ый Код для вывода последовательности, 2-ой для получения суммы
# n = int(input())
# print(end='{')
# print(1, int(1 + 1 / 1) ** 1, sep=':', end=', ')
# for i in range(2, n):
#     print(i, round((1 + 1 / i) ** i, 2), sep=':', end=', ')
# print(n, round((1 + 1 / n) ** n, 2), sep=':', end='}')
# print(sum)

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += (1 + 1 / i) ** i
# print(round(sum, 2))

# 17

# some_list = [-5, 3, 6, 8, 1, 4, 5]
# x = open('x.txt', 'r', encoding='utf-8')
# s = x.read().strip()
# sum = some_list[int(s[0])] * some_list[int(s[2])] * some_list[int(s[4])]
# print(sum)
# x.close()

# 18
# import random
# some_list = [4, 3, 4, 7, 9, 5]
# print(some_list)
#
# for i in range(len(some_list)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     some_list[i], some_list[j] = some_list[j], some_list[i]
#
# print(some_list)




