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
  mu, s2 = theta
  lv = 0
  for i in range(n):
    soma = -(0.5*math.log(2*math.pi*s2))-((1/(2*s2))*(x[i]-mu)**2)
    lv = lv + soma
  return -lv

theta0 = np.array([10,1])
out = optimize.minimize(logvero, theta0, args=(x), method='bfgs', options={'disp': True})
print(out)

theta01 = np.array([1,1])
cons = ((None, None), (0, None))
out1 = optimize.minimize(logvero, theta01, args=(x), method='SLSQP', options={'disp': True},
                         constraints=cons)
