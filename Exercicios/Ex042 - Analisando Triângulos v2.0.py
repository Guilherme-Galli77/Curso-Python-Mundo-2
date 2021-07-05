#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = float(input("Digite o tamanho do primeiro segmento: "))
b = float(input("Digite o tamanho do segundo segmento: "))
c = float(input("Digite o tamanho do terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triangulo! ")
    if a == b == c:
        print("Triângulo EQUILATERO!")
    elif (a == b and a != c) or (b == c and b != a) or (a == c and c != b):
        print("Triangulo ISOCELES!")
    else:
        print("Triangulo ESCALENO!")
else:
    print("Não forma triangulo! ")
