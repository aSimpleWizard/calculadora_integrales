from numpy import arange
from sympy import *
from matplotlib.pyplot import *
from numpy import *

# Pide los limites superior e inferior
print('Ingrese el limite inferior: ')
linf = int(input())
print('Ingrese el limite superior: ')
lsup = int(input())
# Hay que hacer una validacion para que el
# limite superior no sea menor que el inferior, verdad?

# Declarando una funcion que cree a Y que vamos a integrar


def funcion(x):
    # esta es la funcion, hay que hacer que el usuario la ingrese en un textbox o algo xd
    y = 0.3*x**2-x+3
    return y


# montando la grafica
x = arange(linf, lsup, 0.1)
y = funcion(x)

plot(x, y)
fill_between(x, y, where=(linf <= x) & (x <= lsup), color='b', alpha=0.1)
grid()

# integrando
x = symbols('x')
y = funcion(x)
res = integrate(y, (x, linf, lsup))
print(f'la respuesta es {res}')

show()
