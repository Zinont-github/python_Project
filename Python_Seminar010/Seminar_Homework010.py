# class Table:
#     def __init__(self, row, col):
#         self.listt = [[0 for _ in range(col)] for _ in range(row)]
#
#     def get_value(self, row, col):
#         try:
#             if row < 0 or col < 0:
#                 return None
#             else:
#                 return self.listt[row][col]
#         except:
#             None
#
#     def set_value(self, row, col, value):
#         self.listt[row][col] = value
#
#     def n_rows(self):
#         return len(self.listt)
#
#     def n_cols(self):
#         return len(self.listt[0])
#
#     def delete_row(self, row):
#         del self.listt[row]
#
#     def delete_col(self, col):
#         for elem in self.listt:
#             del elem[col]
#
#     def add_row(self, row):
#         self.listt.insert(row, [0 for _ in range(len(self.listt[0]))])
#
#     def add_col(self, col):
#         for elem in self.listt:
#             elem.insert(col, 0)

# Пример 1.
# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(1)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# Пример 2.
# tab = Table(2, 2)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_col(1)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# Пример 3.
# tab = Table(1, 1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 1000)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)

# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


class MinStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt

    def result(self):
        try:
            return min(self.res_listt)
        except:
            return None


class MaxStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt

    def result(self):
        try:
            return max(self.res_listt)
        except:
            return None


class AverageStat:
    def __init__(self):
        self.res_listt = []

    def add_number(self, elem):
        self.res_listt.append(elem)
        return self.res_listt

    def result(self):
        try:
            return sum(self.res_listt) / len(self.res_listt)
        except:
            return None

# Пример 1.
# values = [1, 2, 4, 5]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# Пример 2.
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# print(mins.result(), maxs.result(), average.result())

# Пример 3.
values = [1, 0, 0]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))