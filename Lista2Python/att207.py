lista = [10, 5, 8, 20, 3, 15, 7]

menor_elemento = lista[0]

for numero in lista:
    if numero < menor_elemento:
        menor_elemento = numero

print(f"O menor elemento da lista é: {menor_elemento}")
