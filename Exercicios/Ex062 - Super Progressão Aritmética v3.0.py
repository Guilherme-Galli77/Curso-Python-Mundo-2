#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print("="*30)
print("10 TERMOS DE UMA PA")
print("="*30)
p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
termo = p
contador = 1
total = 0

while contador < 11:
    print("{} -->".format(termo), end="")
    total = total + 1
    termo = termo + r
    contador = contador + 1
print("PAUSA\n")
contador = int(input("Quantos termos você quer mostrar a mais? "))
while contador > 0:
    print("{} -->".format(termo), end="")
    termo = termo + r
    total = total + 1
    contador = contador - 1
    if contador == 0:
        print("PAUSA")
        contador = int(input("Quantos termos você quer mostrar a mais? "))
print("Operação finalizada totalizando {} termos".format(total))





