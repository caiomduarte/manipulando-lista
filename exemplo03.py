
import os

os.system("cls")

print("Como Remover um item na lista")

lista_pokemon = ["Pikachu", "Charmander", "Bubassauro", "Mew", "Squartle"]

# Como remover um item
# lista_pokemon.remove("Bubassauro")
# lista_pokemon.pop(1)

del lista_pokemon[1]

# Excluir a lista inteira
# del lista_pokemon

# Como Esvaziar uma lista
lista_pokemon.clear()


for pokemon in lista_pokemon:
    print("Pokemon: ", pokemon)