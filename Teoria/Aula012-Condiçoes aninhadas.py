nome = str(input("Qual é seu nome? "))
if nome == "Guilherme":
    print("Que nome bonito! ")
elif nome == "Gabriel" or "Joao" or "Maria":
    print("!!!!!!!")
elif nome in 'José Joaquim Paula':
    print("Oi !!!!")
else:
    print("Olá {}".format(nome))

print("Tenha um bom dia, {} ".format(nome))
