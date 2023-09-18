def eh_palindromo(numero):
    numero_str = str(numero)
    
    numero_invertido = numero_str[::-1]

    return numero_str == numero_invertido

numero = int(input("Digite um número: "))

if eh_palindromo(numero):
    print(f"{numero} é um número palíndromo.")
else:
    print(f"{numero} não é um número palíndromo.")
