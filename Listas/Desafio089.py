boletim = list()

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, nota1, nota2])
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()

    while opcao != "S" and opcao != "N":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()

    if opcao == "N":
        break

print("==" * 12, "BOLETIM ESCOLAR", "==" * 12)
print(f"{"Nº":<4} {"Nome":<10} {"Média":>8}")

for i, pos in enumerate(boletim):
    print(f"{i:<4} {pos[0]:<10} {(pos[1] + pos[2]) / 2:>8.2f}")

while True:
    consultar = int(input("As notas de qual aluno gostaria de consultar? (999 para sair) "))

    if consultar == 999:
        break
    if 0 <= consultar < len(boletim):
        print(f"Notas de {boletim[consultar][0]}: {boletim[consultar][1]}, {boletim[consultar][2]}")

print("=" * 66)
print("FIM DO PROGRAMA...")