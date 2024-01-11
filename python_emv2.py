# Objetivo: estimar os parâmetros de uma distribuição normal

# Pacote
import numpy as np
import math
from scipy import optimize
import sys

# Gerar dadosS
x = np.random.normal(10,2,100)

# Logartimo da função de verossimilhança
def logvero(theta,x):
  n = len(x)
  mu = theta[0]
  s = theta[1]  # usando sigma, o método converge para qualquer valor inicial
  soma = sum((x-mu)**2)
  lv = -((n/2)*math.log(2*math.pi))-((n/2)*math.log(s**2))-(soma/(2*(s**2)))
  return -lv

theta0 = [0.1, 0.1]
out = optimize.minimize(logvero, theta0, args=(x), method='bfgs')
print(out)