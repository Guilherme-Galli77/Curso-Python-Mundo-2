num = int(input("Digite um número para ver a sua tabuada: "))
print("="*30)
for c in range(1, 11):
    print("{} X {}  = {} ".format(num, c, (num*c)))
print("="*30)
