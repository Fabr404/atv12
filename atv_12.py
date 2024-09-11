# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
def verificar_aprovacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Receber a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Exibir o resultado
print(f"O aluno está: {verificar_aprovacao(nota)}")
