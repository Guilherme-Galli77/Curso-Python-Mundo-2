#Loop simples
cont = 1
while cont <= 10:
    print(cont, "-->", end="")
    cont += 1
print("FIM")

#Loop infinito, só para manualmente ou com comando break
cont = 1
while True:
    print(cont, "-->", end="")
    cont += 1
print("FIM")

#Teste com entrada de dados infinita até digitar o flag 999

n = 0
while n != 999:
    n = int(input("Digite um número"))



#Teste com entrada de dados em que soma o 999 com outros valores

n = s = 0
while n != 999:
    n = int(input("Digite um número"))
    s += n
print("A soma vale {}".format(s))

#Para remover o 999 da soma da forma correta:
#Soma ocorre e codigo roda normalmente ate digitar 999
n = s = 0
while True:
    n = int(input("Digite um número"))
    if n == 999:
        break
    s += n
print("A soma vale {}".format(s))

#Print com f strings
print(f"A soma vale {s}")

nome = "Jose"
idade = 33
salario = 987.35
print(f"O {nome} tem {idade} anos")
print(f"O {nome} tem {idade} anos e ganha R$ {salario:.2f}")
