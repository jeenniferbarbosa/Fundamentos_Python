# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_col = 0


for linha in range(0, 3):
    for col in range(0, 3):
        valor = int(input(f'Informe os valores para a posição {[linha]}, {[col]}: '))
        matriz[linha][col] = valor

        if valor % 2 == 0:
            soma_pares += valor

print('==' * 15)

for linha in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[linha][col]:^5}]', end=' ')
    print()

for linha in range(3):
    soma_col += matriz[linha][2]

maior_valor = max(matriz[1])

print('==' * 15)

print(f"A soma dos números pares é: {soma_pares}")
print(f"A soma dos números da terceira coluna é: {soma_col}")
print(f"O maior valor da segunda linha é: {maior_valor}")