"""learn lambda function"""
import math
from functools import reduce


def exercise1():
    # перемножает числа списка
    input_list = [3, 5, 6, 7, 8, 2, 4, 3, 4]
    t = reduce(lambda x, y: y * x, input_list)

    t = math.prod(input_list)


def exercise2():
    unsorted_dict = {'фрукт': 'яблоко', 'цвет': 'антрацит', 'артикул': 'в5678',
                     'модель': 'бабочка', 'наименование': 'книга', 'жанр': 'триллер'}

    t = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
    print(t)

    t = dict(sorted(zip(unsorted_dict.values(), unsorted_dict.keys())))
    print(t)


def exercise3():
    inputs = 'физалис груша слива арбуз банан апельсин яблоко папайя'
    lst = list(map(str, inputs.split()))

    output = sorted(list(filter(lambda x: len(x) == 5, lst)))
    print(output)

    output = sorted([t for t in lst if len(t) == 5])
    print(output)


exercise3()
