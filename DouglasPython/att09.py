dividendo = int(input("Digite o dividendo (número a ser dividido): "))
divisor = int(input("Digite o divisor (número pelo qual será dividido): "))

resto = dividendo

while resto >= divisor:
    resto -= divisor

print(f"O resto da divisão de {dividendo} por {divisor} é {resto}")
