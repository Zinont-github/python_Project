import math
# 6

# print('Введите число')
# n = int(input())
# if n > 7 or n < 1:
#     print('Данное число не является днем недели')
# elif n >= 1 and n <= 5:
#     print('нет')
# else:
#     print('да')


# 7

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)


# 8

# print('Введите координату X')
# x = int(input())
#
# print('Введите координату Y')
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# elif x > 0 and y < 0:
#     print('4')
# else:
#     print('Не возможно найти номер четверти')

# 9

# print('Введите номер четверти')
# n = int(input())
# if n == 1:
#     print('Допустимые значения x > 0 y > 0')
# elif n == 2:
#     print('Допустимые значения x < 0 y > 0')
# elif n == 3:
#     print('Допустимые значения x < 0 y < 0')
# elif n == 4:
#     print('Допустимые значения x > 0 y < 0')
# else:
#     print('Нет такой четверти')

# 10

print('Введите координату х первой точки')
x1 = int(input())
print('Введите координату y первой точки')
y1 = int(input())
print('Введите координату х второй точки')
x2 = int(input())
print('Введите координату н первой точки')
y2 = int(input())

length = float((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)) ** 0.5
print(length)
