print("========== Progressão Aritmética ===========")

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao #Formula

for pa in range(termo, decimo + razao, razao):
    print(f"Sequência da PA: {pa}", end=">")

print("FIM")