#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = 0
contPreco = 0
c = 0
continuar = ""

while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))

    total = total + preco
    c = c + 1

    if preco > 1000:
        contPreco += 1

    if c == 1:
        menor = preco
        nomeMenor = nome

    if menor > preco:
        menor = preco
        nomeMenor = nome
    while True:
        continuar = str(input("Você deseja continuar [S/N]? ")).strip().upper()
        if continuar == "S":
            break
        elif continuar == "N":
            break
    if continuar == "N":
        break

print("=====================================================================")
print(f"O total gasto na compra foi de R$ {total:.2f}")
print(f"{contPreco} produtos custam mais de R$ 1000")
print(f"O nome do produto mais barato é {nomeMenor} que custa R$ {menor:.2f}")
