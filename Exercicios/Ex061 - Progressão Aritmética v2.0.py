#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("="*30)
print("10 TERMOS DE UMA PA")
print("="*30)
p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
termo = p
contador = 1

while contador < 11:
        print("{} -->".format(termo), end="")
        termo = termo + r
        contador = contador + 1
print("FIM")