#LISTAS

lista  = ["x",2,True,4.1]
print(lista)

lista[1]*lista[3]

#primeiro nível          0              1              2
#segundo nível      0      1      0     2       0     1     2

lista_nomes = [ ["rodrigo",27],["ana", 98], ["mario", 76, True] ]


for i in range(len(lista_nomes)):
  print(i," ",lista_nomes[i]) 


print(lista_nomes.pop(0)) #Remove elemento da lista  

for i in lista_nomes: #PERCORRE OS ELEMENTOS DA LISTA
  print("Lista = ", i)
  print("Nome = ",i[0])
  print("Idade = ",i[1])
