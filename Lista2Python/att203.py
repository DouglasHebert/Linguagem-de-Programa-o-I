preco_mercadoria = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = (percentual_desconto / 100) * preco_mercadoria

preco_a_pagar = preco_mercadoria - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
