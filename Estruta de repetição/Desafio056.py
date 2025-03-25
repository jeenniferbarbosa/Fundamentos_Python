## Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maior = float('-inf') # Valor infinito (negativo)
nome_masc = ' '
soma = 0
feminino = 0

for pessoa in range(0, 4):
    nome = str(input(f"Informe o nome da {pessoa + 1}º pessoa: "))
    idade = int(input(f"Informe a idade da {pessoa + 1}º pessoa: "))
    sexo = str(input(f"Informe o sexo da {pessoa + 1}º pessoa (F para feminino e M para masculino): ")).upper().strip()
    print('==' * 35)
    soma += idade
    media = soma / 4
    if sexo == 'M' and idade > maior:
        maior = idade
        nome_masc = nome
    if sexo == "F" and idade < 20:
        feminino += 1
print(f"A média de idade é: {media} anos.")
print(f"O nome do homem mais velho é {nome} com {idade} anos.")
print(f"{feminino} mulher(es) tem menos de 20 anos.")