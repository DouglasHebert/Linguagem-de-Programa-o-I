numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

escolha = input("Digite o número da operação desejada (1/2/3/4): ")

if escolha == '1':
    resultado = numero1 + numero2
    operacao = "soma"
elif escolha == '2':
    resultado = numero1 - numero2
    operacao = "subtração"
elif escolha == '3':
    resultado = numero1 * numero2
    operacao = "multiplicação"
elif escolha == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        operacao = "divisão"
    else:
        resultado = "Divisão por zero não é permitida!"
        operacao = "divisão por zero"
else:
    resultado = "Opção inválida"
    operacao = "operação inválida"

print(f"O resultado da {operacao} é: {resultado}")
