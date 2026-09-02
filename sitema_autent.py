usuario_correto = "admin"
senha_correta = "python123"

tentativas = 0
max_tentativas = 3
acesso_liberado = False

while tentativas < max_tentativas:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado! Login realizado com sucesso.")
        acesso_liberado = True
        break
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Usuário ou senha incorretos. Tentativas restantes: {restantes}")
        else:
            print("Acesso bloqueado! Número máximo de tentativas excedido.")

if not acesso_liberado and tentativas == max_tentativas:
    print("Programa encerrado por excesso de tentativas.")
