# Objetivo: tempo necessário para que a concentração da bactéria seja reduzida a
# 9 usando o método da secante (Alt+q para fazer a quebra de texto)

# pacote
import math
from scipy import optimize

# Função f(t)
def f(t):
  y = (70*math.exp(-1.5*t)) + (25*math.exp(-0.075*t))-9
  return y

# Método da secante
optimize.newton(f, x0=10, x1=11, rtol=0.05, full_output=True)

optimize.root_scalar(f, method='secant', x0=10, x1=11, rtol=0.05)