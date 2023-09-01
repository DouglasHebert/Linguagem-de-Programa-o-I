while True:
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha uma opção (1/2/3/4/5): ")

    if escolha == '5':
        print("Programa encerrado.")
        break  # Sai do loop

    numero = int(input("Digite um número para a tabuada: "))

    if escolha == '1':
        for i in range(1, 11):
            print(f"{numero} + {i} = {numero + i}")
    elif escolha == '2':
        for i in range(1, 11):
            print(f"{numero} - {i} = {numero - i}")
    elif escolha == '3':
        for i in range(1, 11):
            print(f"{numero} * {i} = {numero * i}")
    elif escolha == '4':
        for i in range(1, 11):
            if i != 0:
                print(f"{numero} / {i} = {numero / i}")
            else:
                print("Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Escolha uma opção válida (1/2/3/4/5).")
