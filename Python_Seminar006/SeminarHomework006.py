# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
# time_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# import re
#
# i = 0
# while i < len(time_weather):
#     time = re.findall(r'[-+]?\d+',time_weather[i])
#     if not time == []:
#         search_temp = time_weather[i]
#         if not len(search_temp) >1:
#             search_temp = search_temp[:0] + '0' + search_temp[0:]
#             time_weather[i] = search_temp
#         elif search_temp[0] == '+':
#             search_temp = search_temp[:1] + '0' + search_temp[1:]
#             time_weather[i] = search_temp
#         time_weather.insert(i + 1, '"')
#         time_weather.insert(i , '"')
#     if time_weather[i] == '"' and time != []:
#         i += 2
#     else:
#         i += 1
# print(time_weather)
# print(" ".join(time_weather))
#
# time_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# import re
#
# i = 0
# while i < len(time_weather):
#     time = re.findall(r'[-+]?\d+',time_weather[i])
#     if not time == []:
#         search_temp = time_weather[i]
#         if not len(search_temp) >1:
#             search_temp = search_temp[:-1] + '"0' + search_temp[-2:] + '"'
#             time_weather[i] = search_temp
#         elif search_temp[0] == '+' and len(search_temp) == 2:
#             search_temp = search_temp[:0] + '"+0' + search_temp[-1:] + '"'
#             time_weather[i] = search_temp
#         elif search_temp[0] == '+' and len(search_temp) > 2:
#             search_temp =  '"' + search_temp[:] + '"'
#             time_weather[i] = search_temp
#         elif search_temp[0] == '-'and len(search_temp) == 0:
#             search_temp = search_temp[:0] + '"-0' + search_temp[-1:] + '"'
#             time_weather[i] = search_temp
#         elif search_temp[0] == '-' and len(search_temp) > 2:
#             search_temp =  '"' + search_temp[:] + '"'
#             time_weather[i] = search_temp
#         elif len(search_temp) == 2:
#             search_temp = '"' + search_temp[:] + '"'
#             time_weather[i] = search_temp
#     if time_weather[i] == '"' and time != []:
#         i += 2
#     else:
#         i += 1
# print(time_weather)
# print(" ".join(time_weather))

# Дан список, содержащий искажённые данные с должностями и именами сотрудников: ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

# workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
# i = 0
# j = -1
# name = ''
# while i < len(workers):
#     some_workers = workers[i]
#     while some_workers[j] != ' ':
#         name += some_workers[j]
#         j += -1
#
#     new_name = ''.join(reversed(name))
#     new_name_title = new_name.title()
#     workers = [w.replace(new_name, new_name_title) for w in workers]
#     print('Привет, ' + new_name_title)
#
#     name = ''
#     i += 1
#     j = -1
# print(workers)
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# price = [49.8, 30, 6.1, 99.5, 10.3, 52, 124.6, 2.34, 30.1, 55.19]
# last_word = ', '
# price_list_id = id(price)
#
# for i, num in enumerate(price):
#
#     form_price = str(f"{float(num):.2f}").split(".")
#
#     if i == len(price) - 1:
#         last_word = "\n"
#
#     print(f"<<{form_price[0]} руб {form_price[1]} коп>>", end=last_word)
#
# print('')
# print(f"id перед сортировкой {price_list_id}")
# price.sort()
# print(price)
# print(f"id после сортировки {id(price)}")
#
#
# copy_list = price.copy()
# copy_list.sort(reverse=True)
#
# print(copy_list)
# print(price_list_id)
# print(id(copy_list))
#
#
# print("Пять самых дорогих товаров", price[-6:-1])
