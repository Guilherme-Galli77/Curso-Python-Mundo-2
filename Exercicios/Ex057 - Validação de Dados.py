# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input("Informe seu sexo: [M/F] ")).upper().strip()
while s != "M" and s != "F": #pode usar while s not in "MF":
    s = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper().strip()

print("sexo {} registrado com sucesso".format(s))
