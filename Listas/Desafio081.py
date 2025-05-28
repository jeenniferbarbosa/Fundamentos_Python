lista_num = list()

while True:
    num = int(input("Digite um número: "))
    lista_num.append(num)
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    while opcao != "N" and opcao != "S":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    if opcao == "N":
        break

print("==" * 15)
print(f"Foram digitados {len(lista_num)} elementos")
lista_num.sort(reverse=True)
print(f"Em ordem decrescente os valores ficarão: {lista_num}")

if 5 in lista_num:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não está na lista!")

print("==" * 15)

