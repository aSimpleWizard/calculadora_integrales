# Estaba probando algo aquí, ignorar xd

from numpy import arange
from sympy import *
from matplotlib.pyplot import *
from numpy import *

x = arange(0, 10, 0.001)
y = 2*x-3
g = x**2 - 5

# xlim(0, 8)
# ylim(-2, 40)

plot(x, g, x, y)
fill_between(x, y, g, where=(1 <= x) & (x <= 6))


# x = symbols('x')
# y = x**2-2*x
# g = 5*x - 6
# h = g-y
# res = integrate(h, (x, 1, 6))

# print(f'la respuesta es {res}')

grid()
show()
