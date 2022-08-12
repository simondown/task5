import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Button
import keyboard as keyb
from keybind import KeyBinder
from formula import *
from methods import *
from grafik import *
import time

a = 0

b = 0

c = 0

d = 0
points = []
values = []
derives = []
count = 0

delta = 0

def Change_method(event):

    global a

    global axes

    axes.clear()

    if a%3 == 0:
        grafik1(axes, count, points, coef1)

    if a%3 == 1:
        grafik2(axes, count, points, coef2)

    if a%3 == 2:
        grafik3(axes, count, points, coef3, ksi)

    a += 1

def add_delta(event):

    global b

    global delta

    global values
    global coef1
    global coef2
    global coef3

    k = count//2

    if b%2 == 0:

        print("Введите значение дельты:")

        delta = float(input())

        values[k] += delta

        method1(count, points, values, derives, coef1)

        method2(count, points, values, derives, coef2)

        method3(count, points, values, der1, der2, coef3, ksi, M, V)


    if b%2 == 0:

        values[k] -= delta

    else:

        values[k] += delta

    b += 1
    delta = 0

def Change_method_2(event):

    global c

    global axes

    axes.clear()

    if c%4 == 0:
        grafik12(axes, count, points, coef1, coef2)

    if c%4 == 1:
        grafik13(axes, count, points, ksi, coef1, coef3)

    if c%4 == 2:
        grafik23(axes, count, points, ksi, coef2, coef3)

    if c%4 == 3:
        grafik123(axes, count, points, ksi, coef1, coef2, coef3)

    c += 1

def Difference(event):

    global d

    global axes

    axes.clear()

    if d%3 == 0:
        d12(axes, count, points, coef1, coef2)

    if d%3 == 1:
        d13(axes, count, points, ksi, coef1, coef3)

    if d%3 == 2:
        d23(axes, count, points, ksi, coef2, coef3)

    d += 1


def add_point(event):

    global count
    global begin_point
    global end_point
    global points
    global values
    global derives
    global coef1
    global coef2
    global coef3
    global ksi
    global M
    global V
    global a
    global axes

    count += 1

    print("Now count is:", count)

    points = []
    values = []
    derives = []

    step = (end_point - begin_point)/(count-1)

    points.append(begin_point)
    values.append(formula(begin_point))

    _ = 1
    while _ < count-1:

        points.append(begin_point + step*_)
        values.append(formula(points[_]))

        _ += 1

    points.append(end_point)
    values.append(formula(end_point))

    _ = 1
    while _ < count-1:

        derives.append(der_formula(points[_]))

        _ += 1


    derives.insert(0,der1)
    derives.append(der2)

    coef1 = [[0]*4 for _ in range(count-1)]
    coef2 = [[0]*4 for _ in range(count-1)]
    coef3 = [[0]*3 for _ in range(count)]
    ksi = [0]*(count+1)
    M = [[0]*(count+1) for _ in range(count+1)]
    V = [0]*(count+1)

    method1(count, points, values, derives, coef1)
    method2(count, points, values, derives, coef2)
    method3(count, points, values, der1, der2, coef3, ksi, M, V)


    axes.clear()

    if (a-1)%3 == 0:
        grafik1(axes, count, points, coef1)

    if (a-1)%3 == 1:
        grafik2(axes, count, points, coef2)

    if (a-1)%3 == 2:
        grafik3(axes, count, points, coef3, ksi)




print("Введите область приближения")
print("Начальная точка:")
begin_point = float(input())

print("Конечная точка:")
end_point = float(input())

if begin_point >= end_point:

    print("Неправильные данные")
    exit()

print("Введите количество точек приближения")
count = int(input())

print("Выберите способ ввода функции")
print("Введите 1 для ввода из файла")
print("Введите 2 для ввода по формуле")

mode = int(input())

if (mode != 1) and (mode != 2):

    print("Такого способа ввода нет")
    exit()

if mode == 1:

    file = open('dat.txt')
    data = file.read()
    data = list(map(float,data.split()))
    points = [data[0]]
    points += data[2::2]
    values = [data[1]]
    values += data[3::2]

    file.close()

if mode == 2:

    step = (end_point - begin_point)/(count-1)

    points.append(begin_point)
    values.append(formula(begin_point))

    _ = 1
    while _ < count-1:

        points.append(begin_point + step*_)
        values.append(formula(points[_]))

        _ += 1

    points.append(end_point)
    values.append(formula(end_point))


#print("Points are:", points)
#print("Values are:", values)

print("Выберите способ ввода первых производных функции");
print("Введите 1 для ввода из файла");
print("Введите 2 для ввода по формуле");

der_mode = int(input())

if (der_mode != 1) and (der_mode != 2):

    print("Такого способа ввода нет")
    exit()


derives = []

if der_mode == 1:

    file = open("der_dat.txt")

    derives = file.read()
    derives = list(map(float,derives.split()))



if der_mode == 2:

    _ = 1
    while _ < count-1:

        derives.append(der_formula(points[_]))

        _ += 1


#print("Derives are:", derives)

print("Введите значения второй производной в граничных узлах")

der1 = float(input())
der2 = float(input())
derives.insert(0,der1)
derives.append(der2)

#print("Derives now are:", derives)


coef1 = [[0]*4 for _ in range(count-1)]
coef2 = [[0]*4 for _ in range(count-1)]
coef3 = [[0]*3 for _ in range(count)]
ksi = [0]*(count+1)
M = [[0]*(count+1) for _ in range(count+1)]
V = [0]*(count+1)

method1(count, points, values, derives, coef1)
method2(count, points, values, derives, coef2)
method3(count, points, values, der1, der2, coef3, ksi, M, V)


fig, axes = plt.subplots()

fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.2)

axes_button1 = plt.axes([0.43, 0.05, 0.18, 0.075])

button1 = Button(axes_button1, 'Один метод')

button1.on_clicked(Change_method)

axes_button2 = plt.axes([0.03, 0.05, 0.18, 0.075])

button2 = Button(axes_button2, 'Дельта')

button2.on_clicked(add_delta)

axes_button3 = plt.axes([0.23, 0.05, 0.18, 0.075])

button3 = Button(axes_button3, 'Два метода')

button3.on_clicked(Change_method_2)

axes_button4 = plt.axes([0.63, 0.05, 0.18, 0.075])

button4 = Button(axes_button4, 'Разница')

button4.on_clicked(Difference)

axes_button5 = plt.axes([0.83, 0.05, 0.18, 0.075])

button5 = Button(axes_button5, 'Добавить точку')

button5.on_clicked(add_point)




plt.show()
#plt.subplot(1,3,2)

#grafik2(count, points, coef2)

#plt.subplot(1,3,3)

#grafik3(count, points, coef3, ksi)

#keyb.add_hotkey('1', isPressed1(a, count, points, coef1, coef2, coef3, ksi))

#plt.show()

#keyb.wait()
