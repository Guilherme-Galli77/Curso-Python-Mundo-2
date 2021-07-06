frase = str(input("Digite uma frase: ")).strip().replace(" ", "").upper()
inverso = ""

for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
print("O inverso de {} é {}".format(frase, inverso))
if inverso == frase:
    print("Temos um palindromo")
else:
    print("Não é palindromo")


