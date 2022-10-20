# 22
# list = [2, 5, 3, 7, 1, 9]
# sum = 0
#
# for i in range(1, len(list), 2):
#     sum += int(list[i])
#
# print(sum)

# 23

# list1 = [3, 4, 5, 7, 8, 10, 12, 2, 6, 4, 3]
# list2 = list(map(int, list1))
# list3 = []
# for i in range(0, int(int(len(list1)) / 2)):
#     if int(len(list1)) % 2 == 0:
#         list3.append(list2[i] * list2[-i - 1])
#     else:
#         list3.append(list2[i] * list2[-i - 1])
# if int(len(list1)) % 2 != 0:
#         list3.append(list2[int(int(len(list1)) / 2)] ** 2)
#
# print(list3)
#
# 24

# number = [1.2, 5.5, 8.02, 3.05]
# number = list(map(float, number))
# max = [0]
# min = [1]
# print(number [2] % 1 > number[0] % 1)
# print()
# for i in range(0, len(number)):
#     if (number[i] % 1) > max[0]:
#         max[0] = (number[i] % 1)
#     if (number[i] % 1) < min[0]:
#         min[0] = (number[i] % 1)
# print(round(max[0] - min[0], 2))


# # 25
# n = int(input())
# list = []
# while n != 0:
#     list.append(n % 2)
#     n //= 2
# list.reverse()
# print(list)