#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print("Sou seu computador! ")
print("-="*40)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-="*40)

num = ""
cont = 0

while num != computador:
    num = int(input("Qual é seu palpite? "))
    cont = cont + 1
    if num > computador:
        print("Menos... Tente mais uma vez")
    elif num < computador:
        print("Mais... Tente mais uma vez")

print("Acertou com {} tentativas!".format(cont))
