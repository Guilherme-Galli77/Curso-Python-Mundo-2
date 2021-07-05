#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
print("Quem nasceu em {} tem {} anos em {} ".format(ano, idade, date.today().year))

if idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(18-idade))
    print("Seu alistamento será em {}".format(date.today().year + (18-idade)))
elif idade == 18:
    print("Você tem {} anos e está na hora de se alistar! ".format(idade))
else:
    print("Você passou em {} anos o prazo de se alistar".format(idade-18))
