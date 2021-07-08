#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
dezoito = h = m20 = 0

while True:
    print("=================================")
    print("     CADESTRE UMA PESSOA         ")
    print("=================================")

    idade = int(input("Idade: "))
    s = str(input("Sexo: [M/F]: ")).upper().strip()
    if idade >= 18:
        dezoito = dezoito + 1
    if s == "M":
        h = h + 1
    if s == "F" and idade < 20:
        m20 = m20 + 1
    print("=================================")

    cont = str(input("Quer continuar [S/N] ? ")).upper().strip()
    if cont == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {dezoito}")
print(f"Ao todo temos {h} homens cadastrados")
print(f"E temos {m20} mulheres com menos de 20 anos")
