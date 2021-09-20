from copy import copy
from sympy import symbols, simplify


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

    print(f'wd = {wd:.3f}\nsum(yi/wi) = {sum(yw):.3f}\np({f}) = {wd * sum(yw):.5f}')


def newton_interpolator(x: [], y: [], interpolator: float, degree: int):
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

    for v in range(degree):
        print(f'    delta {v}  ', end='')

    print('\n', '-' * 12, '-' * 12 * degree)

    for k in range(len(box) - 1):
        temp = []
        for l in range(len(box) - k - 1):
            print(f'{box[l][k]:11.3f}  ', end='')
            temp.append(box[l][k])
        boxt.append(temp)
        print()

    print(f'f({interpolator}) = ', end='')

    for w in range(degree + 1):
        if w == 0:
            r = boxt[0][w]
            print(f'{boxt[0][w]}', end='')
        else:
            temp = 1
            print(' + ' if boxt[0][w] > 0 else ' - ', f'{abs(boxt[0][w])}', end='')
            for z in range(0, w):
                temp *= (interpolator - x[z])
                print(f'({interpolator - x[z]})', end='')

            r += (boxt[0][w] * temp)

    print()
    print(f'f({interpolator}) = {simplify(r)}')


lagrange_interpolator(x=[0, 1, 3],
                      y=[5, 5, 11],
                      f=2)

print()

newton_interpolator(x=[-0.256, -0.039, 0.233, 0.562],
                    y=[1.5, 1.6, 1.7, 1.8],
                    interpolator=symbols('x'),
                    degree=3)

print()

newton_interpolator(x=[-0.256, -0.039, 0.233, 0.562],
                    y=[1.5, 1.6, 1.7, 1.8],
                    interpolator=0,
                    degree=3)

print()

newton_interpolator(x=[-1, 0, 1, 2],
                    y=[2, 1, 0, 4],
                    interpolator=-2,
                    degree=3)
