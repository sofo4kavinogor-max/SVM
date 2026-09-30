import math

def f(x):
    return math.cos(x) - x

def proiz(x):
    return -math.sin(x) - 1

def fi(x):
    return math.cos(x)

def bisec(a, b, eps):
    if f(a) * f(b) >= 0:
        print("Метод не применим: f(a) и f(b) одного знака")
        return None
    
    count = 0
    
    while True:
        c = (a + b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        count += 1
        if abs(a - b)/2 < eps:
            break
    return c, count


def hord(a, b, eps):
    count = 0
    x_0 = a
    while True:
        x_k = a - f(a)*(b-a)/(f(b)-f(a))

        if abs(x_k - x_0) < eps:
            break
        count += 1
        if f(a) * f(x_k) < 0:
            b = x_k
        else:
            a = x_k

        x_0 = x_k
    return x_k, count

def Neut(p, eps):
    count = 0
    x_k = p

    while True:
        x_k1 = x_k - f(x_k)/proiz(x_k)

        if abs(x_k1 - x_k) < eps:
            break
        count += 1
        x_k = x_k1
    return x_k1, count 

def Iter(p, eps):
    count = 0
    x_k = p

    while True:
        x_k1 = fi(x_k)

        if abs(x_k1 - x_k) < eps:
            break
        x_k = x_k1
        count += 1
    return x_k1, count

print('Бисекция для 10^-3: ', bisec(0, 1, 10**-3))
print('Бисекция для 10^-5: ', bisec(0, 1, 10**-5))

print('Хорды для 10^-3: ', hord(0, 1, 10**-3))
print('Хорды для 10^-5: ', hord(0, 1, 10**-5))

print('Ньютон для 10^-3, приближение 0,5: ', Neut(0.5, 10**-3))
print('Ньютон для 10^-5, приближение 0,5: ', Neut(0.5, 10**-5))
    
print('Ньютон для 10^-3, приближение 1: ', Neut(1, 10**-3))
print('Ньютон для 10^-5, приближение 1: ', Neut(1, 10**-5))    

print('Простые итерации для 10^-3, приближение 0.5: ', Iter(0.5, 10**-3))
print('Простые итерации для 10^-3, приближение 1: ', Iter(1, 10**-3))

print('Простые интерации для 10^-5, приближение 0.5: ', Iter(0.5, 10**-5))
print('Простые интерации для 10^-5, приближение 1: ', Iter(1, 10**-5))