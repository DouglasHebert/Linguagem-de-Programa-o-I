def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 24.9:
        categoria = "Peso normal"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    elif imc < 34.9:
        categoria = "Obesidade grau I"
    else:
        categoria = "Obesidade grau II"

    return imc, categoria

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros, por favor: "))

imc, categoria = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
print(f"Você está na categoria: {categoria}")
