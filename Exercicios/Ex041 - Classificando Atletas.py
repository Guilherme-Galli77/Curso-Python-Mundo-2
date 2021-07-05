#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano = int(input("Ano de Nascimento: "))
esseAno = date.today().year
idade = esseAno - ano
print("O atleta tem {} anos ".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif 9 < idade <= 14:
    print("Classificação: INFANTIL")
elif 14 < idade <= 19:
    print("Classificação: JUNIOR")
elif 19 < idade <= 25:
    print("Classificação: SENIOR")
else:
    print("Classificação: MASTER")
