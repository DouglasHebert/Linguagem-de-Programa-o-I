contagem = 0
soma = 0
numeros = []

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break 
    
    numeros.append(numero)
    soma += numero
    contagem += 1

if contagem > 0:
    media = soma / contagem
else:
    media = 0

print(f"Quantidade de números digitados: {contagem}")
print(f"Soma dos números digitados: {soma}")
print(f"Média aritmética dos números digitados: {media:.2f}")
