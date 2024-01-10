# Objetivo: tempo necessário para que a concentração da bactéria seja reduzida a
# 9 usando o método de Newton (Alt+q para fazer a quebra de texto)

# pacote
import math
from scipy import optimize

# Função f(t)
def f(t):
  y = (70*math.exp(-1.5*t)) + (25*math.exp(-0.075*t))-9
  return y

# Derivada da função
def fl(t):
  y = -(150*math.exp(-1.5*t)) - (1.875*math.exp(-0.075*t))
  return y

# Método de Newton
root = optimize.newton(f, 10, rtol=0.05, fprime=fl)
print(round(root, 8))

optimize.newton(f, 10, rtol=0.05, fprime=fl,full_output=True)

optimize.root_scalar(f, method='newton', x0=10, fprime=fl, rtol=0.05)