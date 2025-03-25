# Soma de números pares

soma = 0
cont = 0

for c in range(0, 6):
    num = int(input("Digite um valor: R$ "))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f"Entre os valores citados apenas {cont} são pares. A soma desses valores é: {soma}")