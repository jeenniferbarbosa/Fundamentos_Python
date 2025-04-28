classificacao_brasileirao_2025 = ('Flamengo', 'Palmeiras', 'Red Bull Bragantino', 'Cruzeiro', 'Fluminense',
                                'Internacional', 'Bahia', 'Botafogo', 'Ceará', 'São Paulo', 'Vasco da Gama', 'Corinthians',
                                'Juventude', 'Mirassol', 'Fortaleza', 'Vitória', 'Atlético-MG', 'Santos', 'Grêmio', 'Sport')

print("===" * 15)
print(f"    Classificação Brasileirão 2025      ")
print("===" * 15)
print(f"Times classificados: {classificacao_brasileirao_2025} ")
print("===" * 15)
print(f"Os 5 primeiros times são: {classificacao_brasileirao_2025[0:5]}")
print("===" * 15)
print(f"Os últimos 4 colocados são: {classificacao_brasileirao_2025[16:20]} ")
print("===" * 15)
print(sorted(classificacao_brasileirao_2025))
print("===" * 15)

time = "Chapeconse"
if time in classificacao_brasileirao_2025:
    print(f"O time {time} está classificado na posição: {classificacao_brasileirao_2025.index(time) + 1}")
else:
    print("O time Chapecoense não está classificado.")