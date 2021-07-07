#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

seq = "S"
cont = 0
soma = 0

while seq == "S":
    numero = int(input("Digite um número: "))
    cont += 1
    soma = soma + numero
    media = soma/cont
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    seq = str(input("Quer continuar? [S/N] ")).strip().upper()

print("Você digitou {} números e a media foi {:.2f} ".format(cont, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
