def multiplicar(a , b): #Criando a função multiplicar
  c = a *b
  return c

#RESOLVER A EQUAÇÃO
#  = ax² + bx +c

def calcdelta(lista_coeficientes): #Criando a função calcdelta
  a = lista_coeficientes[0]
  b = lista_coeficientes[1]
  c = lista_coeficientes[2]

  delta = b**2 - 4*a*c
  return delta

def calcx(lista_coeficientes): #Criando a função calcx
  a = lista_coeficientes[0]
  b = lista_coeficientes[1]
  c = lista_coeficientes[2]

  x1 = (-b + calcdelta(lista_coeficientes)**(1/2))/(2*a)
  x2 = (-b - calcdelta(lista_coeficientes)**(1/2))/(2*a)
  return x1, x2

#UTILIZANDO AS FUNÇÕES------------------------------------------
print( multiplicar(2,3))

# Y = -2X² + 3X + 5
coeficientes=[-2, 3, 5] 

print(calcdelta(coeficientes))
print(calcx(coeficientes))
