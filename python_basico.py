# Objetivo: aprender os comandos básicos em python

# lista de string
frutas = ["morango", "pera", "melancia"]
print(frutas)

# lisa de inteiros
x = [10, 2, 3]
print(x)
x[0] # pyhton começa a contagem do 0

# Variavel global
y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y)

# If e else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# while
i = 1
while i < 6:
  print(i)
  i += 1

# for
for x in range(6): # range(6) = [0,1,2,3,4,5,6]; range(2,6) = [2,3,4,5,6]
  print(x)

# Importar pacotes
import math

math.exp(2)

# Para instalar pacote
# ... Terminal New Terminal
# py -m pip install nome_pacote

import numpy as np

# Vetor como uma linha
vl = np.array([1, 2, 3])
print(vl)
vl[1]

# Vetor como coluna
vc = np.array([[1],
               [2],
               [3]])
print(vc)
vc[1,0]

# Matriz
matriz = np.array([[1, 2],
                   [1, 4],
                   [1, 2]])

print(matriz)
matriz[1,1]

# selecao de elementos
z = np.array([10,20,30,40,50])
# selecionar elementos a partir do terceiro elementos
z[2:]
# selecionar os dois primeiros elementos
z[:2]
# selecionar a primeira coluna
matriz[:,0]
# selecionar a seguna linha
matriz[1,:]

# Função soma
def soma(x):
  n = len(x)
  y = 0
  for i in range(n):
    y = y + x[i]
    i += 1
  return y

k1 = np.array([1, 2, 3])

k2 = [1, 2, 4]

soma(k1)

# Observação: quando shift+enter não estiver lendo a proxima linha, excluir a
# pasta .vscode