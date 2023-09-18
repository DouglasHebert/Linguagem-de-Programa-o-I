texto = input("Digite uma string: ")

contagem_caracteres = {}

for caractere in texto:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

for caractere, contagem in contagem_caracteres.items():
    print(f"{caractere}: {contagem}x")
