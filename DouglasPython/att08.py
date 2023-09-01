numero1 = input("Digite um número de 1 a 10 : ")
numero2 = input("Digite outro número de 1 a 10 : ")

caracteres_comuns = ""

for char in numero1:
    if char in numero2 and char not in caracteres_comuns:
        caracteres_comuns += char

if caracteres_comuns:
    print("Caracteres comuns aos dois números :", caracteres_comuns)
else:
    print("Não há caracteres comuns nos dois números.")
