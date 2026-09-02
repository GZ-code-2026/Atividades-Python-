alunos = {}

for i in range(10):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

notas = list(alunos.values())

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

aprovados = 0
recuperacao = 0
reprovados = 0

print("\n--- Situação por aluno")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} ({nota}): Aprovado")
        aprovados += 1
    elif nota >= 5 and nota < 7:
        print(f"{nome} ({nota}): Recuperação")
        recuperacao += 1
    else:
        print(f"{nome} ({nota}): Reprovado")
        reprovados += 1

# Relatório final
print("\n--- Relatório Geral")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
