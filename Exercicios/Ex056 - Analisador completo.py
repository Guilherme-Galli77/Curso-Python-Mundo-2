#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

totIdade = 0
contM = 0
hMaisVelho = ""
idadeH = 0
for pessoa in range(1, 5):
    print("-------------{} PESSOA-------------".format(pessoa))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    totIdade = totIdade + idade
    if sexo == "M":
        if idade > idadeH:
            hMaisVelho = nome
            idadeH = idade
    if sexo == "F" and idade < 20:
        contM = contM + 1

print("A média de idade do grupo é de {} anos".format(totIdade/4))
print("O homem mais velho tem {} anos e se chama {}".format(idadeH, hMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(contM))
