#SOLUÇÃO DA EQUAÇÃO DE 2 GRAU
import numpy as np
#Definir os valores
a=1
b=-5
c=2
# Calcular delta
delta = (b**2)-(4*a*c)
#Verificar o numero de raizes
if delta <0:
  print("Não possui raizes reais")
elif delta == 0: # == é utilizado para verificar igualdade
  print("Possui apenas uma raiz real")
else:
  print("Possui duas raizes reais")
#Calcular as raizes
if delta >= 0:
  raizdelta=np.sqrt(delta)
  x1 = (-b + raizdelta)/(2*a)
#SOLUÇÃO DA EQUAÇÃO DE 2 GRAU
import numpy as np
#Definir os valores
a=1
b=-5
c=2
# Calcular delta
delta = (b**2)-(4*a*c)
#Verificar o numero de raizes
if delta <0:
  print("Não possui raizes reais")
elif delta == 0: # == é utilizado para verificar igualdade
  print("Possui apenas uma raiz real")
else:
  print("Possui duas raizes reais")
#Calcular as raizes
if delta >= 0:
  raizdelta=np.sqrt(delta)
  x1 = (-b + raizdelta)/(2*a)
  x2 = (-b - raizdelta)/(2*a)
  #Apresentar os resultados
  print("As raizes são:", round(x1,2), round(x2,2))
