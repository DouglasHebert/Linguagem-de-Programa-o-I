distancia = float(input("Digite a distância a percorrer em quilômetros: "))

velocidade_media = float(input("Digite a velocidade média esperada para a viagem em km/h: "))

tempo_em_horas = distancia / velocidade_media

tempo_em_minutos = tempo_em_horas * 60

print(f"O tempo de viagem será de aproximadamente {tempo_em_horas:.2f} horas ou {tempo_em_minutos:.2f} minutos.")
