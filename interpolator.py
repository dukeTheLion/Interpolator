from math import factorial
from copy import copy
from sympy import symbols, simplify


def mean(lst: []):
    return sum(lst) / len(lst)


def lagrange_interpolator(x: [], y: [], f: float):
    aux = f
    wd = 1
    yw = []
    wi = []

    for i in x:
        print(f'{i:11.3f}  ', end='')
    print(f'       wi          yi/wi')
    print('-' * 13 * len(x), '-' * 24)

    for i in range(len(x)):
        temp = 1
        for j in range(len(x)):
            if i == j:
                aux = f
            else:
                aux = x[i]

            temp *= (aux - x[j])
            print(f'{(aux - x[j]):11.4f}  ', end='')

            if i == j:
                wd *= (aux - x[j])

        wi.append(temp)
        yw.append(y[i] / temp)
        print(f'{temp:11.3f}  {y[i] / temp:11.3f}')

    print(f'wd = {wd:.3f}\nsum(yi/wi) = {sum(yw):.3f}\np({f}) = {wd * sum(yw):.5f}\n')
    print('-' * 110, '->\n')


def newton_interpolator(x: [], y: [], interpolator: float):
    box = [copy(y)]
    boxt = []
    r = 0

    for i in range(len(x)):
        temp = []
        for j in range(0, len(x) - i - 1):
            val = (box[i][j + 1] - box[i][j])
            val = val / (x[j + i + 1] - x[j])
            temp.append(val)
        box.append(temp)

    print('       y     ', end='')

    for v in range(len(x) - 1):
        print(f'    delta {v}  ', end='')

    print('\n', '-' * 12, '-' * 12 * (len(x) - 1))

    for k in range(len(box) - 1):
        temp = []
        for l in range(len(box) - k - 1):
            print(f'{box[l][k]:8.2f}  ', end='')
            temp.append(box[l][k])
        boxt.append(temp)
        print()

    print(f'\nf({interpolator}) = ')

    for w in range(len(x)):
        if w == 0:
            r = boxt[0][w]
            print(' + ' if boxt[0][w] > 0 else ' - ', f'{abs(boxt[0][w])}')
        else:
            temp = 1
            print(' + ' if boxt[0][w] > 0 else ' - ', f'{abs(boxt[0][w])}', end='')
            for z in range(0, w):
                temp *= (interpolator - x[z])
                print(f'({interpolator - x[z]})', end='')
            print()

            r += (boxt[0][w] * temp)

    print()
    print(f'f({interpolator}) = {simplify(r)}\n')
    print('-' * 110, '->\n')


def gregory_newton_interpolator(x: [], y: [], interpolator: float):
    box = [copy(y)]
    boxt = []
    r = 0
    h = x[1] - x[0]
    z = (interpolator - x[0]) / h

    for i in range(len(x)):
        temp = []
        for j in range(0, len(x) - i - 1):
            val = (box[i][j + 1] - box[i][j])
            temp.append(val)
        box.append(temp)

    print('       y     ', end='')

    for v in range(len(x) - 1):
        print(f'    delta {v}  ', end='')

    print('\n', '-' * 12, '-' * 12 * (len(x) - 1))

    for k in range(len(box) - 1):
        temp = []
        for l in range(len(box) - k - 1):
            print(f'{box[l][k]:11.3f}  ', end='')
            temp.append(box[l][k])
        boxt.append(temp)
        print()

    print(f'\nf({interpolator}) = ')

    for w in range(len(x)):
        if w == 0:
            r = boxt[0][w]
            print(' + ' if boxt[0][w] > 0 else ' - ', f'{abs(boxt[0][w])}')
        else:
            temp = 1
            print(' + ' if boxt[0][w] > 0 else ' - ', f'({abs(boxt[0][w])} * ', end='')
            for q in range(0, w):
                temp *= (z - q)
                print(f'({(z - q)})', end='')
            print(f')/{factorial(w)}')

            r += ((boxt[0][w] / factorial(w)) * temp)

    print()
    print(f'f({interpolator}) = {simplify(r)}')
    print('-' * 110, '->\n')


lagrange_interpolator(x=[4,7,10],
                      y=[35,28,25],
                      f=5)


"""newton_interpolator(x=[-0.256, -0.039, 0.233, 0.562],
                    y=[1.5, 1.6, 1.7, 1.8],
                    interpolator=symbols('x'))


newton_interpolator(x=[-0.256, -0.039, 0.233, 0.562],
                    y=[1.5, 1.6, 1.7, 1.8],
                    interpolator=0)"""

"""gregory_newton_interpolator(x=[0, 15, 30, 45, 60],
                            y=[112.5-50, 154.5-86, 195-146, 171-73.5, 95.5-50],
                            interpolator=35)"""

"""newton_interpolator(x=[-1, 0, 0.5, 0.8, 1.2, 1.3, 1.5, 1.8, 2, 3],
                    y=[7, 5, 6.25, 7.72, 10.52, 11.37, 13.25, 16.52, 19, 35],
                    interpolator=symbols('x'))"""
