cont = 0
valor_total = 0
menor_valor = float("inf")
produto_menor_valor = " "

while True:
    print("------------------" * 2)
    print("       LOJÃO TECH+       ")
    print("------------------" * 2)
    produto = str(input("Nome do produto adquirido: "))
    valor_produto = float(input("Valor do produto: R$ "))
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    valor_total = valor_total + valor_produto
    while opcao != "N" and opcao != "S":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    if valor_produto > 1000.00:
        cont += 1
    if valor_produto < menor_valor:
        produto_menor_valor = produto
        menor_valor = valor_produto
    if opcao == "N":
        break

print(f"O valor total de sua compra foi: R${valor_total: .2f} ")
print(f"{cont} produtos custaram mais de R$ 1000,00 reais.")
print(f"O produto de menor custo é {produto_menor_valor} custando R${menor_valor: .2F} reais.")
