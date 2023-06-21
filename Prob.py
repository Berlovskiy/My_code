import numpy as np
from math import sin
import matplotlib.pyplot as plt
from random import randint
import json


def get_x(num, quant):
    lst_x = []
    const = abs(num)
    while num <= const:
        lst_x.append(num)
        num += (abs(const*2))/quant
    return lst_x


def get_param4func(lst):
    def get_points(func):
        def wrapper(*args, **kwargs):
            lst_y = []
            for i in lst:
                lst_y.append(func(args[0], args[1], i, args[2]))
            return lst_y
        return wrapper
    return get_points


x = get_x(-5, 150)


@get_param4func(x)
def sin_f(a, w, x, f):
    return a*sin(w*x + f)


@get_param4func(x)
def quad(a, b, x, c):
    return a*x*x + b*x + c


#y_1 = sin_f(150, 2, 8)
#y_2 = quad(2, 4, 6)
#plt.plot(x, y_1)
#plt.plot(x, y_2)
#plt.show()


def get_plot(func_1, func_2, n):
    func_list = [func_1, func_2]
    annot_arr = np.zeros(7)
    aumont = randint(2, 7)
    annot_arr[aumont - 1] = 1
    for i in range(aumont):
        par_1 = randint(1, 30)
        par_2 = randint(1, 30)
        par_3 = randint(1, 100)
        plt.plot(x, func_list[randint(0, 1)](par_1, par_2, par_3))

    return plt.savefig(f'{aumont}.figure {n}.png'), annot_arr


dataset = {'figures': []}
for i in range(3000):
    json_obj = {}
    json_obj['title'] = f'figure {i}'
    json_obj['annotation'] = list(get_plot(sin_f, quad, i)[1])
    dataset['figures'].append(json_obj)
    plt.close()

data = json.dumps(dataset)
data = json.loads(str(data))
with open('data_set.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)

