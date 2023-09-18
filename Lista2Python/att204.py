quilometros_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

custo_por_dia = 65
custo_por_km = 0.25

preco_a_pagar = (dias_aluguel * custo_por_dia) + (quilometros_percorridos * custo_por_km)

print(f"O preço a pagar pelo aluguel do carro é de R$ {preco_a_pagar:.2f}")
