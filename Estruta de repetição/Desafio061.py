print("========== Progressão Aritmética 2.0 ===========")

primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
termo = primeiro
cont = 0

while cont < 10:
    print(f"{termo}", end=" >> ")
    termo += razao
    cont += 1

print("Fim do programa.")