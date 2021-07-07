#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

c = True
x = float(input("Primeiro valor: "))
y = float(input("Segundo valor: "))
while c == True: #Posso usar um while opcao !=5
    print("""
    ======================================================================================
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opcao = int(input("QUAL È A SUA OPÇÃO? "))
    if opcao == 1:
        soma = x + y
        print("A soma entre {} + {} é {}".format(x, y, soma))
    elif opcao == 2:
        multi = x * y
        print("A multiplicacao entre {} X {} é {}".format(x, y, multi))
    elif opcao == 3:
        if x > y:
            print("O maior entre {} e {} é o {}".format(x, y, x))
        elif y > x:
            print("O maior entre {} e {} é o {}".format(x, y, y))
        else:
            print("{} e {} são iguais".format(x, y))
    elif opcao == 4:
        print("Digite os novos numeros: ")
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))
    elif opcao == 5:
        print("Obrigado!!")
        c = False
    else:
        print("Opção inválida!!!")