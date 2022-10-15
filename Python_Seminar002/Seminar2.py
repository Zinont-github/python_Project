# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81
# n = int(input())
# s = 1
# print(s, end = ' ')
# for i in range(1, n):
#     s = s * -3
#     print(s, end = ' ')

# n = int(input())
# for i in range(n - 1):
#     print((-3) ** i, end=', ')
# print((-3) ** (n - 1))

# n = int(input())
# a = []
# for i in range(n):
#     a.append((-3) ** i)
# print(*a, sep=', ')


# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#
#     *Пример:*
#
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input())
# print('{' , end= '')
# for i in range(1, n):
#     print(i, 3 * i + 1,  sep=':', end=', ')
# print(n, 3 * n + 1, end='}')

# n = int(input())
# print('{', end='')
# for i in range(1, n):
#     print(f'{i}:{3 * i + 1}', end=', ')
# print(f'{n}:{3 * n + 1}', end='}')


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой

# text1 = input()
# text2 = input()
# print(str1.count(str2))
#
# for i in range(len(str1)):
#
#
# count = 0
# for i in range(len(text1)):
#     if text1[i] == text2[0]:
#         if text1[i:i + len(text2)] == text2:
#             count += 1
#
# print(count)

# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#     if some_str_1[i:i + len_str_2] == some_str_2:
#         count += 1
#     i += 1
# print(count)


# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#    if some_str_1[i:i + len_str_2] == some_str_2:
#       count += 1
#        i += len_str_2
#    else:
#        i += 1
# print(count)









