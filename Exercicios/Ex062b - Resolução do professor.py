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
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print("{} -->".format(termo), end="")
        termo += r
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("PA finalizada com {} termos mostrados".format(total))
