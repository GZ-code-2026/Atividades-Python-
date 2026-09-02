nome_aluno = input("Digite o nome do aluno que deseja consultar: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
qtd_faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and qtd_faltas <= 10:
    print(f"{nome_aluno}, você foi aprovado com média {media:.2f} e {qtd_faltas} faltas.")

elif media >= 5 and media < 6.9 and qtd_faltas <= 10:
    print(f"{nome_aluno}, você está de recuperação com média {media:.2f} e {qtd_faltas} faltas.")
elif media < 5 or qtd_faltas > 10:
    print(f"{nome_aluno}, você foi reprovado com média {media:.2f} e {qtd_faltas} faltas.")

else:
    print("Dados inválidos.")

    