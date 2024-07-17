
import os

os.system("cls")

print("Como Classificar uma lista")

lista_filmes = ["a lagoa azul", "rambo", "Missão Impossivel", "Titanic"]

lista_filmes.sort()

lista_numeros = [299, 10,1,0,1990]

#lista_numeros.sort(reverse = True)

lista_numeros.reverse()

for filme in lista_filmes:
    print("Filme: ", filme)