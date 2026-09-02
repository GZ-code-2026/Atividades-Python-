def validar_senha(senha):
    requisitos_atendidos = []
    requisitos_faltando = []

    # Pelo menos 8 caracteres
    if len(senha) >= 8:
        requisitos_atendidos.append("tamanho mínimo")
    else:
        requisitos_faltando.append("pelo menos 8 caracteres")

    # Pelo menos uma letra
    if any(c.isalpha() for c in senha):
        requisitos_atendidos.append("letra")
    else:
        requisitos_faltando.append("pelo menos uma letra")

    # Pelo menos um número
    if any(c.isdigit() for c in senha):
        requisitos_atendidos.append("número")
    else:
        requisitos_faltando.append("pelo menos um número")

    # Pelo menos um caractere especial
    caracteres_especiais = "!@#$%^&*()-_=+[]{};:,.<>?/\\|~`'\""
    if any(c in caracteres_especiais for c in senha):
        requisitos_atendidos.append("caractere especial")
    else:
        requisitos_faltando.append("pelo menos um caractere especial")

    # Resultado
    if not requisitos_faltando:
        print("Senha Forte!")
    else:
        print("Senha Fraca. Requisitos não atendidos:")
        for requisito in requisitos_faltando:
            print(f"- {requisito}")


# Teste
senha_digitada = input("Digite uma senha para validar: ")
validar_senha(senha_digitada)