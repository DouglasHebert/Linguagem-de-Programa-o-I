valor_casa = float(input("Digite o valor da casa a comprar: R$ "))
salario = float(input("Digite o seu salário mensal: R$ "))
anos_a_pagar = int(input("Digite a quantidade de anos a pagar: "))

meses_a_pagar = anos_a_pagar * 12

prestacao_maxima = salario * 0.3

prestacao = valor_casa / meses_a_pagar

if prestacao <= prestacao_maxima:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {prestacao:.2f}")
else:
    print("Empréstimo negado. O valor da prestação excede 30% do seu salário.")
