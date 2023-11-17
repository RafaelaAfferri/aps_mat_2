import math
e = math.e

def calcula_a_b(ponto):
    a = 2 * ponto[0] + ponto[1] - 1
    b = ponto[0] + 8 * ponto[1] - 4
    return a, b

def calcula_modulo(a, b):
    return math.sqrt(a**2 + b**2)

def calcula_x1_y1(a, b, alpha, ponto):
    x1 = ponto[0] - alpha * a
    y1 = ponto[1] - alpha * b
    return x1, y1

def calcula_a_b_2(ponto):
    a = ponto[0]/(math.sqrt(ponto[0]**2 + ponto[1]**2 + 2) + 2* (e**(-ponto[1]**2))+2*(ponto[0]-2))
    b = ponto[1]/(math.sqrt(ponto[0]**2 + ponto[1]**2 + 2)) - 2* (e**(-ponto[1]**2))+ponto[0]**2 * ponto[1]

    return a, b

