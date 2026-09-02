Consumo_mensal = []

for i in range(6):
    consumo = float(input(f"Digite o consumo de luz no mês {i+1}: "))
    Consumo_mensal.append(consumo)

consumo_medio = sum(Consumo_mensal) / len(Consumo_mensal)
maior_consumo = max(Consumo_mensal)
menor_consumo = min(Consumo_mensal)
meses_acima_media = sum(1 for c in Consumo_mensal if c > consumo_medio)

print(f"Consumo médio: {consumo_medio:.2f}")
print(f"Maior consumo: {maior_consumo:.2f}")
print(f"Menor consumo: {menor_consumo:.2f}")
print(f"Meses acima da média: {meses_acima_media}")

# Desafio extra
posicao_maior = Consumo_mensal.index(maior_consumo) + 1
print(f"O maior consumo ocorreu no mês {posicao_maior}")
