#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m",end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")

print("\n\033[mO número {} foi divisivel {} vezes".format(num, tot))
if tot == 2:
    print("O número é primo")
else:
    print("o numero não é primo")
