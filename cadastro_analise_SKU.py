cadastro_Produto = {}

quantidade = int(input("Quantos produtos serão cadastrados? "))

if quantidade > 5:
    print("Quantidade inválida. O programa será encerrado.")
    exit()

for i in range(quantidade):
    print(f"\n--- Cadastro do produto {i+1} de {quantidade} ---")

    nome_produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade_estoque = int(input("Digite a quantidade em estoque: "))

    cadastro_Produto[nome_produto] = {
        "preco": preco,
        "quantidade_estoque": quantidade_estoque,
    }

# Análise dos produtos
mais_caro = max(cadastro_Produto, key=lambda p: cadastro_Produto[p]["preco"])
mais_barato = min(cadastro_Produto, key=lambda p: cadastro_Produto[p]["preco"])

valor_total_geral = 0

print("\n--- Valor total do estoque por produto ---")
for produto, dados in cadastro_Produto.items():
    valor_estoque = dados["preco"] * dados["quantidade_estoque"]
    valor_total_geral += valor_estoque
    print(f"{produto}: R$ {valor_estoque:.2f}")

print(f"\nProduto mais caro: {mais_caro} (R$ {cadastro_Produto[mais_caro]['preco']:.2f})")
print(f"Produto mais barato: {mais_barato} (R$ {cadastro_Produto[mais_barato]['preco']:.2f})")
print(f"Valor total de todo o estoque: R$ {valor_total_geral:.2f}")