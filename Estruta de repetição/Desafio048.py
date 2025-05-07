#"Soma entre números múltiplos de três, em um intervalo de 1 a 500

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print(f"A soma entre todos os {cont} valores é: {soma}")