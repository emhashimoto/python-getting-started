# Objetivo: fazer uma simulação de monte carlo

# Pacote
import numpy as np
import math
from scipy import optimize
import statistics as stat

# Número de simulações
r = 5
# Tamanho da amostra
n = 100
# Vetor de estimativas
vmu = np.zeros(r)
vs = np.zeros(r)

def logvero(theta,x):
  mu = theta[0]
  s = theta[1]
  soma = sum((x-mu)**2)
  lv = -((n/2)*math.log(2*math.pi))-((n/2)*math.log(s**2))-(soma/(2*(s**2)))
  return -lv

j = 0
while j < r:
  # Gerar dados
  x = np.random.normal(10,2,n)
  theta0 = [0.1, 0.1]
  out = optimize.minimize(logvero, theta0, args=(x), method='bfgs')
  if out.success == True:
    print('------', j, '------')
    print(out.message)
    print(out.status)
    vmu[j] = out.x[0]
    vs[j] = out.x[1]
    print('Estimativa de mi:', vmu[j])
    print('Estimativa de mi:', vs[j])
    j += 1
  else:
    j += j

stat.mean(vmu)
stat.mean(vs)