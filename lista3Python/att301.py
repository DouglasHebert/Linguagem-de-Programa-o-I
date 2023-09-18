def encontrar_maior_menor(lista):
    if len(lista) == 0:
        return None, None
    maior = menor = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor

entrada = input("Digite uma lista de números separados por espaços: ")

numeros = [float(numero) for numero in entrada.split()]

maior, menor = encontrar_maior_menor(numeros)

if maior is not None and menor is not None:
    print(f"O maior valor é: {maior}")
    print(f"O menor valor é: {menor}")
else:
    print("A lista está vazia.")