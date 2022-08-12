import math

def formula(x):
    return math.sin(x)

def der_formula(x):
    return -math.cos(x)

def diff(x1, x2, y1, y2):

    return (y2-y1)/(x2-x1)

def weight (i, points, values):

    return abs(diff(points[i], points[i+1], values[i], values[i+1]) - diff(points[i-1], points[i], values[i-1], values[i]))

def new_cub(_, points, coef, x):

    return coef[_][0] + coef[_][1]*(x - points[_]) + coef[_][2]*(x - points[_])*(x - points[_]) + coef[_][3]*(x - points[_])*(x - points[_])*(x - points[_])

def new_par(_, coef, points, ksi, x):

    return coef[_][0] + coef[_][1]*(x - ksi[_]) + coef[_][2]*(x - ksi[_])*(x - points[_])

