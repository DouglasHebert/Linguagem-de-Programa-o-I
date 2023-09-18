cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Digite quantos anos você já fumou: "))

minutos_perdidos_por_cigarro = 12
total_minutos_perdidos = cigarros_por_dia * minutos_perdidos_por_cigarro * 365 * anos_fumados

dias_perdidos = total_minutos_perdidos / (24 * 60)  

print(f"Um fumante perderá aproximadamente {dias_perdidos:.2f} dias de vida devido ao hábito de fumar.")
