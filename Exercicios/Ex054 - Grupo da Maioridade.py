#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totMaior = 0
totMenor = 0
for pessoas in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pessoas)))
    if (date.today().year - nasc) >= 18:
        print("Maior de idade")
        totMaior += 1
    else:
        print("Menor de idade")
        totMenor += 1
print("A quantidade de maiores de idade foi de {} pessoas".format(totMaior))
print("A quantidade de menores de idade foi de {} pessoas".format(totMenor))

