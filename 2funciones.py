from numpy import arange
from sympy import *
from matplotlib.pyplot import *
from numpy import *


print('Ingrese el limite inferior: ')
linf = int(input())
print('Ingrese el limite superior: ')
lsup = int(input())

# Funcion 1
def funcion(x):
    y = x**2 + 2*x + 3
    return y

# Funcion 2
def funcion2(x):
    g = x + 9
    return g


# montando la grafica
x = arange(linf, lsup, 0.1)
y = funcion(x)
g = funcion2(x)

plot(x, y, x, g)
fill_between(x, y, g, where=(linf <= x) & (x <= lsup), color='b', alpha=0.1)
grid()

# integrando
x = symbols('x')
y = funcion(x)
g = funcion2(x)

h = g-y

print(h)
res = integrate(h, (x, linf, lsup))
print(f'la respuesta es {res}')

show()
