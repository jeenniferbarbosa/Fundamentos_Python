# Estrura de repetição (FOR)

## Contagem regressiva
# for c in range(6, 0, -1):
#     print(c)
# print("FIM")

## Pulando de 2 em 2
# for c in range(0, 7, 2):
#     print(c)
# print("FIM")

## Entrada do usuário
# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Pulo: "))
# for c in range(i, f + 1, p):
#     print(c)
# print("FIM")

## Entrada do usuário dentro do laço
soma = 0
for c in range(0, 5):
    entrada = int(input("Digite um valor: "))
    soma += entrada
print(f"A soma de todos os valores é: {soma}")