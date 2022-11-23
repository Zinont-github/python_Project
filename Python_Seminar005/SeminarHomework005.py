# 38
# text = open('file.txt', 'r')
# text2 = text.readline()
# text3 = text.readline()
# text3 = text3.split()
# new_text = list(filter(lambda i: 'abc' not in i, text3))
# print(new_text)

# 42


#
# def rle(txt):
#     number_sim = ''
#     prev_char = ''
#     count = 1
#
#     if not txt: return ''
#
#     for char in txt:
#         if char != prev_char:
#             if prev_char:
#                 number_sim += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         number_sim += str(count) + prev_char
#         return number_sim
#
# f = open('file.txt', 'r')
# string = f.read()
# print(rle(string))