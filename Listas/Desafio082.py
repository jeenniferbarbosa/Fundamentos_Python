lista_num = list()
lista_pares = list()
lista_impares = list()

while True:
    num = int(input("Digite um número: "))
    lista_num.append(num)
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    while opcao != "N" and opcao != "S":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    if opcao == "N":
        break

print("==" * 25)
print(f"Os números informados foram: {lista_num}")
print(f"Os números pares são: {lista_pares}")
print(f"Os números impares são: {lista_impares}")
print("==" * 25)