num_ext = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete",
           "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",
           "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

print("=+=" * 18)

while True:
    num = int(input("Digite um número entre 0 e 20 e o veja por extenso: "))
    while num > 20 or num < 0:
        num = int(input("Número inválido tente novamente. Informe um número entre 0 e 20: "))
    print(f"Você digitou o número {num_ext[num]}")
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    print("=+=" * 18)
    while opcao != "N" and opcao != "S":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    if opcao == "N":
        break

print("Programa finalizado")