valor_inicial = int(input("Digite o valor inicial da dívida: R$ "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (%): "))
valor_mensal_pago = int(input("Digite o valor mensal que será pago: R$ "))

numero_meses = 0
total_pago = 0

while valor_inicial > 0:
    juros = int(valor_inicial * (taxa_juros_mensal / 100))
    valor_total_mensal = valor_mensal_pago + juros  
    if valor_total_mensal <= juros:
        valor_necessario = valor_inicial + juros
        print(f"O valor mensal pago não é suficiente para cobrir os juros. Para pagar a dívida, o pagamento mensal deve ser de pelo menos R$ {valor_necessario}")
        break
    valor_inicial += juros
    valor_inicial -= valor_mensal_pago
    numero_meses += 1
    total_pago += valor_total_mensal

if valor_inicial <= 0:
    print(f"Número de meses para pagar a dívida: {numero_meses} meses")
    print(f"Total pago: R$ {total_pago}")
