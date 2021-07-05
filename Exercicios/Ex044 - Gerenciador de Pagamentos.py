#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros


print("===========LOJA===========")
preco = float(input("Preço das compras: R$ "))
print("FORMAS DE PAGAMENTO")
print("""
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    final = preco*0.90
elif opcao == 2:
    final = preco*0.95
elif opcao == 3:
    final = preco
    parcela = final / 2
    print("Sua compra sera parcelada em 2x de R$ {} ".format(parcela))
elif opcao == 4:
    final = preco*1.20
    totalParc = int(input("Quantas parcelas? "))
    parcela = final / totalParc
    print("Sua compra será parcelada em {} X de R${:.2f} COM JUROS ".format(totalParc, parcela))
else:
    final = preco
    print("Opção inválida! ")

print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final ".format(preco, final))