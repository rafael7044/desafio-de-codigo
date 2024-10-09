
faturamento_diario = [
    1500, 2200, 0, 1800, 2000, 3000, 1200, 0, 3100, 200, 1000, 2500, 2900, 0,
    1700, 2100, 0, 3400, 1500, 0, 500, 2700, 0, 2100, 2800, 1300, 2200, 0, 0, 1600
]

# Remover dias com faturamento igual a 0
dias_com_faturamento = [dia for dia in faturamento_diario if dia > 0]

# Calcular o menor valor de faturamento
menor_faturamento = min(dias_com_faturamento)

# Calcular o maior valor de faturamento
maior_faturamento = max(dias_com_faturamento)

# Calcular a média de faturamento mensal (considerando dias com faturamento)
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contar o número de dias com faturamento superior à média
dias_acima_da_media = len([dia for dia in dias_com_faturamento if dia > media_mensal])

# Exibir os resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
