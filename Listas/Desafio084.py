# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()

# Adicionando dados à lista
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    opcao = str(input("Gostaria de continua [s/n]? ")).upper().strip()

    while opcao != "S" and opcao != "N":
        opcao = str(input("Gostaria de continua [s/n]? ")).upper().strip()
    dados.clear()

    if opcao == "N":
        break

maior = pessoas[0][1]
menor = pessoas[0][1]
pessoas_maior_peso = list()
pessoas_menor_peso = list()

# Verificando o peso
for pessoa in pessoas:
    peso = pessoa[1]
    nome = pessoa[0]

    if peso > maior:
        maior = peso
        pessoas_maior_peso = [nome]
    elif peso == maior:
        pessoas_maior_peso.append(nome) # Adiciona mais um nome com o peso igual

    if peso < menor:
        menor = peso
        pessoas_menor_peso = [nome]
    elif peso == menor:
        pessoas_menor_peso.append(nome)

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso é {maior}kg da(s) seguinte(s) pessoa(s): {pessoas_maior_peso}")
print(f"O menor peso é {menor}kg da(s) seguinte(s) pessoa(s): {pessoas_menor_peso}")