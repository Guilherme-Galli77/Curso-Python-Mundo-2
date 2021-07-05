# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from random import choice

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
opcao = int(input("Qual é a sua jogada? "))
print("""JO
KEN
PO!!!!""")

if opcao == 0:
    jogador = "pedra"
elif opcao == 1:
    jogador = "papel"
elif opcao == 2:
    jogador = "tesoura"

jogadas = ["pedra", "papel", "tesoura"]
maquina = random.choice(jogadas)

if jogador == "pedra" and maquina == "tesoura":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Jogador venceu!")
elif jogador == "papel" and maquina == "pedra":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Jogador venceu!")
elif jogador == "tesoura" and maquina == "papel":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Jogador venceu!")
elif jogador == "pedra" and maquina == "papel":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Computador venceu!")
elif jogador == "papel" and maquina == "tesoura":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Computador venceu!")
elif jogador == "tesoura" and maquina == "pedra":
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("Computador venceu!")
else:
    print("====================================")
    print("Computador jogou {} ".format(maquina))
    print("Jogador jogou {} ".format(jogador))
    print("====================================")
    print("O jogo empatou!")
