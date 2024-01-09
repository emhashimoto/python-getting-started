# Objetivo: aprender os comandos básicos em python

# lista
frutas = ["morango", "pera", "melancia"]
print(frutas)

# vetor numerico
x = [10, 2, 3]
print(x)
x[0]

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

np.abs(-20)

