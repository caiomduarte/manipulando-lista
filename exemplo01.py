
import os

os.system("cls")

print("Manipulando Listas")

# Criando uma lista
carros = ["Gol", "Fusca", "Uno", "Fiorino"]

# Exibir todos os itens de uma lista
for carro in carros:
    print("Elemento: " , carro)

# Exibindo o carro que está na posicao 3
print("O carro que está na posicao 3: ", carros[3])
print("O carro que está na posicao 2: ", carros[2])

# Como Alterar um item na lista
carros[0] = "Lamborghini"
carros[1] = "Ferrari"
carros[2] = "Porshe"
carros[3] = "Land Rover"

# Como alterar um intervalo de itens na lista
carros[1:3] = ["Bugati", "Mustang"]

print("Exibindo a lista com itens alterados")
print("======================================")
# Exibir todos os itens de uma lista
for carro in carros:
    print("Elemento: " , carro)


# Como retornar o tamanho de uma lista
print(len(carros))

input("Pressione <ENTER> para continuar")