from formula import *
import numpy as np

def method1(count, points, values, derives, coef1):

    derives[0] = (3*diff(points[0], points[1], values[0], values[1]) - (derives[0]*(points[1] - points[0]))/2 - derives[1])/2;

    derives[count-1] = (3*diff(points[count-2], points[count-1], values[count-2], values[count-1]) + (derives[count-1]*(points[count-1] - points[count-2]))/2 - derives[count-2])/2;

#    print(derives)
#    print(points)
#    print(values)

    i=0

    while i < count-1:

        coef1[i][0] = values[i]

        coef1[i][1] = derives[i]

        coef1[i][2] = (3*diff(points[i], points[i+1], values[i], values[i+1]) - 2*derives[i] - derives[i+1])/(points[i+1]-points[i])

        coef1[i][3] = (derives[i] + derives[i+1] - 2*diff(points[i], points[i+1], values[i], values[i+1])) / ((points[i+1] - points[i]) * (points[i+1] - points[i]))

        i += 1

#    print(coef1)


def method2(count, points, values, derives, coef2):

    x0 = points[0] - (points[1] - points[0])
    xn = points[count-1] + (points[count-1] - points[count-2])
    f0 = values[0] - (values[1] - values[0])
    fn = values[count-1] + (values[count-1] - values[count-2])

    w0 = 0
    wn = 0

    i = 2

    while i < count-2:

        if(weight(i, points, values) != 0):# не та проверка

            derives[i] = ((weight(i+1, points, values)*diff(points[i-1], points[i], values[i-1], values[i]) + weight(i-1, points, values)*diff(points[i], points[i+1], values[i], values[i+1]))/(weight(i+1, points, values) + weight(i-1, points, values)))

        else:

            derives[i] = (((points[i+1] - points[i])*diff(points[i-1], points[i], values[i-1], values[i]) + (points[i] - points[i-1])*diff(points[i], points[i+1], values[i], values[i+1]))/(points[i+1] - points[i-1]))

        i += 1

    w0 = abs(diff(points[0], points[1], values[0], values[1]) - diff(x0, points[0], f0, values[0]))

    wn = abs(diff(points[count-1], xn, values[count-1], fn) - diff(points[count-2], points[count-1], values[count-2], values[count-1]))

    if w0 != 0:

        derives[0] = (weight(1, points, values)*diff(x0, points[1], f0, values[0]) + w0*diff(points[0], points[1], values[0], values[1]))/(weight(1, points, values)+w0)

    else:

        derives[0] = ((points[1] - points[0])*diff(x0, points[0], f0, values[0]) + (points[0] - x0)*diff(points[0], points[1], values[0], values[1]))/(points[1] - x0)

    if wn != 0:

        derives[count-1] = ((wn*diff(points[count-2], points[count-1], values[count-2], values[count-1]) + weight(count-2, points, values))/(wn+weight(count-2, points, values)))

    else:

        derives[count-1] = ((xn - points[count-1])*diff(points[count-2], points[count-1], values[count-2], values[count-1]) + (points[count-1] - points[count-2])*diff(points[count-1], xn, values[count-1], fn))/(xn - points[count-2])

#    print("now derives are", derives)

    i=0

    while i < count-1:

        coef2[i][0] = values[i]

        coef2[i][1] = derives[i]

        coef2[i][2] = (3*diff(points[i], points[i+1], values[i], values[i+1]) - 2*derives[i] - derives[i+1])/(points[i+1]-points[i])

        coef2[i][3] = (derives[i] + derives[i+1] - 2*diff(points[i], points[i+1], values[i], values[i+1])) / ((points[i+1] - points[i]) * (points[i+1] - points[i]))

        i += 1

#    print(coef2)

def method3(count, points, values, der1, der2, coef3, ksi, M, V):

    _ = 1
    while _ < count:
        ksi[_] = (points[_-1] + points[_])/2
        _ += 1

    ksi[0] = points[0] - 0.1
    ksi[count] = points[count-1] + 0.1

#    print("кси равны ",ksi)
#    print("Points are:", points)
#    print("Values are:", values)

    M[0][0] = 2/((ksi[1]-ksi[0])*(points[0]-ksi[0]))
    M[0][1] = 2/((ksi[1]-ksi[0])*(ksi[1]-points[0]))
    M[count][count-1] = 2/((ksi[count]-ksi[count-1])*(points[count-1]-ksi[count-1]))
    M[count][count] = 2/((ksi[count]-ksi[count-1])*(ksi[count]-points[count-1]))

    V[0] = der1 + (2*values[0]/(ksi[1]-ksi[0]))*(1/(points[0]-ksi[0])+1/(ksi[1]-points[0]))

    V[count] = der2 + (2*values[count-1]/(ksi[count] - ksi[count-1]))*(1/(points[count-1]-ksi[count-1])+1/(ksi[count]-points[count-1]))

    i = 1
    while i < count:

        M[i][i-1] = 1/(points[i-1] - ksi[i-1]) - 1/(ksi[i] - ksi[i-1])

        M[i][i] = 1/(ksi[i] - points[i-1]) + 1/(ksi[i] - ksi[i-1]) + 1/(points[i] - ksi[i]) + 1/(ksi[i+1] - ksi[i])

        M[i][i+1] = 1/(ksi[i+1] - points[i]) - 1/(ksi[i+1] - ksi[i])

        V[i] = values[i-1]*(1/(points[i-1] - ksi[i-1]) + 1/(ksi[i] - points[i-1])) + values[i]*(1/(points[i] - ksi[i]) + 1/(ksi[i+1] - points[i]))

        i += 1

    X = np.linalg.solve(M,V)

    list(X)

#    print(M)
#    print(V)
#    print("Vector is", X)

    for i in range(1, count):

#        coef3[i][0] = X[i]

#        coef3[i][1] = (values[i]-X[i])/(points[i]-ksi[i]) - (points[i]-ksi[i])/(ksi[i+1]-ksi[i])*((X[i+1]-values[i])/(ksi[i+1]-points[i]) - (values[i]-X[i]/(points[i]-ksi[i])))

#        coef3[i][2] = 1/(ksi[i+1]-ksi[i])*((X[i+1]-values[i])/(ksi[i+1]-points[i]) - (values[i]- X[i])/(points[i]-ksi[i]))
        coef3[i][0] = X[i]

        coef3[i][1] = (values[i] - X[i])/(points[i] - ksi[i])

        coef3[i][2] = 1/(ksi[i+1]-ksi[i])*((X[i+1]-values[i])/(ksi[i+1]-points[i]) - (values[i] - X[i])/(points[i] - ksi[i]))

#    print(coef3)

