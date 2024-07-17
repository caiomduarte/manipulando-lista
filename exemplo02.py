
import os

os.system("cls")

print("Como Adicionar um Novo item Na lista")
lista_frutas = ["Maça", "Banana", "Acerola"]
# Adicionando um novo Item
lista_frutas.insert(2, "Manga")
# Adicionar um item no final da lista
lista_frutas.append("Morango")
# Como acrescentar elementos de outra lista em uma lista atual
lista_frutas_tropicais = ["Abacaxi", "Laranja", "Melancia"]
lista_frutas.extend(lista_frutas_tropicais)

# Exibindo itens da lista
for fruta in lista_frutas:
    print("Fruta: ", fruta)

print("==================================")
print("Lista de frutas tropicais") 

for fruta_tropical in lista_frutas_tropicais:
     print("Fruta Tropical: ", fruta_tropical)

input("Pressione <Enter> para continuar")