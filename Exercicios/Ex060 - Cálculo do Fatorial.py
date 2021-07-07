#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#MEU METODO
num = int(input("Digite um número para calcular seu fatorial: "))
mult = 1
while num > 0:
    mult = num*mult
    num = num - 1
    print(num+1," X ", end="")
print(" = {}".format(mult))

#METODO PROFESSOR --> SIMPLIFICADO

from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}".format(n, f))

#METODO PROFESSOR --> METODO TRADICIONAL

x = int(input("Digite um número para calcular seu fatorial: "))
c = x
f = 1
print("Calculando {}! = ".format(x))
while c > 0:
    print("{} x".format(c),end="")
    print(" X " if c > 1 else " = ",end="")
    f = f * c
    c -= 1
print("{}".format(f))
