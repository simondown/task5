import numpy as np
import math
import matplotlib.pyplot as plt
from formula import *

def grafik1(axes, count, points, coef1):

#    axes.title('Эрмит')

    _ = 0
    while _ < count - 1:

        x = np.linspace(points[_], points[_+1])

        y = new_cub(_, points, coef1, x)

        _ += 1

        axes.plot(x,y, color = 'r', label = 'Эрмит')


def grafik2(axes, count, points, coef2):


#    plt.title('Акима')

    _ = 0
    while _ < count - 1:

        x = np.linspace(points[_], points[_+1])

        y = new_cub(_, points, coef2, x)

        _ += 1

        axes.plot(x,y, color = 'b', label = 'Акима')

#    axes.legend()

def grafik3(axes, count, points, coef3, ksi):

#    plt.title('Парабола')

    _ = 0
    while _ < count:

        x = np.linspace(ksi[_], ksi[_+1])

        y = new_par(_, coef3, points, ksi, x)

        axes.plot(x, y, color = 'g', label = 'Парабола')

        _ += 1

def grafik12(axes, count, points, coef1, coef2):

    _ = 0
    while _ < count - 1:

        x = np.linspace(points[_], points[_+1])

        y1 = y = new_cub(_, points, coef1, x)

        y2 = new_cub(_, points, coef2, x)

        _ += 1

        axes.plot(x,y1,'r', x, y2, 'b')

def grafik13(axes, count, points, ksi, coef1, coef3):

    i = 0
    j = 0

    while i < count - 1:

        x1 = np.linspace(points[i], points[i+1])

        y1 = new_cub(i, points, coef1, x1)

        i += 1

        axes.plot(x1, y1, 'r')

    while j < count:

        x2 = np.linspace(ksi[j], ksi[j+1])

        y2 = new_par(j, coef3, points, ksi, x2)

        j += 1

        axes.plot(x2, y2, 'g')

def grafik23(axes, count, points, ksi, coef2, coef3):

    i = 0
    j = 0

    while i < count - 1:

        x1 = np.linspace(points[i], points[i+1])

        y1 = new_cub(i, points, coef2, x1)

        i += 1

        axes.plot(x1 ,y1, 'b')

    while j < count:

        x2 = np.linspace(ksi[j], ksi[j+1])

        y2 = new_par(j, coef3, points, ksi, x2)

        j += 1

        axes.plot(x2, y2, 'g')

def grafik123(axes, count, points, ksi, coef1, coef2, coef3):

    i = 0
    j = 0

    while i < count - 1:

        x1 = np.linspace(points[i], points[i+1])

        y1 = new_cub(i, points, coef1, x1)

        y2 = new_cub(i, points, coef2, x1)

        i += 1

        axes.plot(x1 ,y1, 'r', x1, y2, 'b')

    while j < count:

        x3 = np.linspace(ksi[j], ksi[j+1])

        y3 = new_par(j, coef3, points, ksi, x3)

        j += 1

        axes.plot(x3, y3, 'g')


def d12(axes, count, points, coef1, coef2):

    _ = 0
    while _ < count - 1:

        x = np.linspace(points[_], points[_+1])

        y1 = new_cub(_, points, coef1, x)

        y2 = new_cub(_, points, coef2, x)

        _ += 1

        axes.plot(x, abs(y1-y2), 'r')


def d13(axes, count, points, ksi, coef1, coef3):

    i = 0

    while i < count - 1:

        x1 = np.linspace(points[i], points[i+1])

        y1 = new_cub(i, points, coef1, x1)

        y2 = new_par(i, coef3, points, ksi, x1)

        i += 1

        axes.plot(x1 , abs(y1-y2), 'b')

def d23(axes, count, points, ksi, coef2, coef3):

    i = 0

    while i < count - 1:

        x1 = np.linspace(points[i], points[i+1])

        y1 = new_cub(i, points, coef2, x1)

        y2 = new_par(i, coef3, points, ksi, x1)

        i += 1

        axes.plot(x1 , abs(y1-y2), 'g')







