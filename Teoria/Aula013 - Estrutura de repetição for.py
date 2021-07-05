print("Oi")
print("Oi")
print("Oi")
print("Oi")
print("Oi")
print("Oi")
print("========================")
for c in range(0, 6): #Print do valor 6 vezes
    print("Oi")
print("FIM")
print("========================")
for c in range(1, 6): #Print do valor 5 vezes pois ele ignora o ultimo valor
    print(c)
print("FIM")
print("========================")
for c in range(6, 0, -1): #Print do valor 6 vezes contando pra trás e -1 é a iteração
    print(c)
print("FIM")
print("========================")
for c in range(0, 7, 2): #Print do valor contando com passo 2 em 2
    print(c)
print("FIM")
print("========================")
print("========================")
print("========================")
print("========================")
####################################################################
n = int(input("Digite um número: ")) #Conta até o número digitado
for c in range(0, n+1):
    print(c)
print("FIM")
##################################################################
print("========================")
print("========================")
print("========================")
print("========================")
###################################################################
#Codigo para determinar sequencia e passo de um contador
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range (i, f+1, p):
    print(c)
print("FIM")
##################################################################
print("========================")
print("========================")
print("========================")
print("========================")
###################################################################
for c in range(0, 3): #Executa 3 vezes o comando dentro do for
    n = int(input("Digite um valor: "))
print("FIM")
##################################################################
print("========================")
print("========================")
print("========================")
print("========================")
###################################################################
#Contador com somatória de valores
s = 0
for c in range(0, 4):
    z = int(input("Digite um valor"))
    s = s + z #Ou s+=n
print("O somatório de todos os valores foi {}".format(s))

