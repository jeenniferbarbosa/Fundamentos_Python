print("========== Progressão Aritmética 3.0 ===========")

primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
termo = primeiro
cont = 1
cont_termo = 0
termo_mais = 10
total = 0
while termo_mais != 0:
    total = total + termo_mais
    while cont <= total:
        print(f"{termo}", end=" >> ")
        termo += razao
        cont += 1
    print("Pausa")
    termo_mais = int(input("Quantos termos a mais você quer mostrar? "))
print(f"A progressão foi finalizado mostrando {total} termos.")
print("Fim do programa.")