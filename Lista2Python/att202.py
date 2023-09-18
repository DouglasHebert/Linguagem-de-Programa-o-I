materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))
materia4 = float(input("Digite a nota da matéria 4: "))
materia5 = float(input("Digite a nota da matéria 5: "))

media = (materia1 + materia2 + materia3 + materia4 + materia5) / 5

if media > 7:
    print(f"O aluno foi aprovado com média {media:.2f}")
else:
    print(f"O aluno não foi aprovado com média {media:.2f}")
