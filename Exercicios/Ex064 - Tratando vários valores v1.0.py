#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
cont = 0
soma = 0

while numero != 999:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero != 999:
        soma = soma + numero
        cont += 1
print("Você digitou {} números e a soma entre eles foi de {} ".format(cont, soma))