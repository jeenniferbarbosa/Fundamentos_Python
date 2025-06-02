lista_num = list()

while True:
    num = (int(input("Informe um número: ")))
    if num not in lista_num:
        lista_num.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor já informado anteriormente. Informe outro.")

    opcao = str(input("Gostaria de continuar? [s/n]: ")).upper().strip()

    while opcao != "S" and opcao != "N":
        opcao = str(input("Gostaria de continuar? [s/n]: ")).upper().strip()
    if opcao == "N":
        break

print("===" * 25)
lista_num.sort()
print(f"Você informou os seguintes números: {lista_num}")
print("===" * 25)