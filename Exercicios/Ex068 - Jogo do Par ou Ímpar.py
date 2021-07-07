#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
import random
computador = ""
vitorias = 0
derrota = 0
while True:
    jogador = str(input("PAR ou IMPAR? ")).upper().strip()
    while True:
        if jogador == "PAR":
            computador = "IMPAR"
            break
        elif jogador == "IMPAR":
            computador = "PAR"
            break
        else:
            print("Erro!!")
            jogador = str(input("PAR ou IMPAR? ")).upper().strip()

    jogada = int(input("Digite um numero aleatório de 0 a 10"))
    maquina = random.randint(0, 10)

    if (maquina + jogada) % 2 == 0:
        print("PAR ganhou")
        ganhou = "PAR"
        if jogador == ganhou:
            vitorias = vitorias + 1
            print("JOGADOR GANHOU")
        else:
            print("COMPUTADOR GANHOU")
            derrota = 1

    else:
        print("IMPAR ganhou")
        ganhou = "IMPAR"
        if jogador == ganhou:
            vitorias = vitorias + 1
            print("JOGADOR GANHOU")
        else:
            print("COMPUTADOR GANHOU")
            derrota = 1

    if derrota == 1:
        break

print(f"O total de vitorias consecutivas foi {vitorias}")
