for c in range(1, 10):
    print(c)
print("FIM")

x = 1
while x < 10:
    print(x)
    x = x +1
print("FIM")

#######################################
print("==============================")
#######################################
for c in range(1, 5):
    n = int(input("Digite um valor: "))
print("FIM")

# Nao sei o tamanho da operacao, por isso uso while
# So para quando digitar 0, com for nao seria possivel fazer dessa forma
n = 1
while n != 0:
    n = int(input("Digite um valor"))
print("FIM")


# So para quando resp for diferente de S, com for nao seria possivel fazer dessa forma
resp ="S"
while resp == "S":
    n = int(input("Digite um valor"))
    resp = str(input("Continuar? S ou N ?")).upper()
print("FIM")

#Com while posso realizar operacoes que eu nao sei quantas n vezes vou precisar repetir ela, ou que esse valor seja
#indeterminado seguindo uma certa condição

#######################################
print("==============================")
#######################################

y = 1
par = impar = 0
while y !=0:
    y = int(input("Digite um valor: "))
    if y != 0:
        if y % 2 == 0:
            par += 1
        else:
            impar += 1

print("Pares: {}".format(par))
print("Impares: {}".format(impar))
print("Acabou")
