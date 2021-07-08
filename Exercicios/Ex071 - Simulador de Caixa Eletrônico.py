#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
nota50 = nota20 = nota10 = nota1 = 0


print("==============================")
print("           BANCO              ")
print("==============================")

valor = int(input("Que valor você quer sacar? R$  "))
tot = valor

while True:
    if tot >= 50:
        nota50 += 1
        tot -= 50
    elif tot >= 20:
        nota20 += 1
        tot -= 20
    elif tot >= 10:
        nota10 += 1
        tot -= 10
    elif tot >= 1:
        nota1 += 1
        tot -= 1
    if tot == 0:
        break

print("==============================")
print("        NOTAS SACADAS         ")
print("==============================")
print(f"{nota50} Cédulas de R$ 50")
print(f"{nota20} Cédulas de R$ 20")
print(f"{nota10} Cédulas de R$ 10")
print(f"{nota1} Cédulas de R$ 1")