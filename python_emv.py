# Objetivo: estimar os parâmetros de uma distribuição normal

# Pacote
import numpy as np
import math
from scipy import optimize

# Gerar dados
x = np.random.normal(10,1,100)

# Logartimo da função de verossimilhança
def logvero(theta,x):
  n = len(x)
  mu = theta
  s2 = 1
  lv = 0
  for i in range(n):
    soma = -0.5*math.log(2*math.pi*s2)-((1/(2*s2))*(x[i]-mu)**2)
    lv = lv + soma
  return -lv

out = optimize.minimize(logvero, 1, args=(x), method='bfgs')
print(out)
