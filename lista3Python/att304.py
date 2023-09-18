n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("O fatorial é indefinido para números negativos.")
else:
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i

    print(f"O fatorial de {n} é {fatorial}")
