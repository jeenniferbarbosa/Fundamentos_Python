# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("====" * 6)
print("      CAIXA SAQ+     ")
print("====" * 6)
valor_de_saque = int(input("Qual o valor você deseja sacar? R$ "))
cedulas_disp = [50, 20, 10, 1]
while valor_de_saque > 0:
    for cedula in cedulas_disp:
        quantidade = valor_de_saque // cedula
        if quantidade > 0:
            print(f"Total de cédulas de R${cedula}: {quantidade}")
            valor_de_saque %= cedula