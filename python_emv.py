# Objetivo: estimar os parâmetros de uma distribuição normal

# Pacote
import numpy as np

# Gerar dados
x = np.random.normal(10,1,100)

# Logartimo da função de verossimilhança
def lv(theta):
  