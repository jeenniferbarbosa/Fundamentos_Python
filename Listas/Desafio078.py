valores = list()
menor = 0
maior = 0

for cont in range(0, 5):
    valores.append(int(input(f"Informe o valor da posição {cont}: ")))
    if cont == 0:
        menor = maior = valores[cont]
    else:
        if valores[cont] < menor:
            menor = valores[cont]
        if valores[cont] > maior:
            maior = valores[cont]


print("====" * 12)
print(f"Você informou os valores: {valores}")
print("====" * 12)

print(f"O menor valor digitado foi {menor} na posição ", end="")

for pos, valor in enumerate(valores):
    if valor == menor:
        print(f"{pos}...", end="")

print(f"\nO maior valor digitado foi {maior} na posição ", end="")

for pos, valor in enumerate(valores):
    if valor == maior:
        print(f"{pos}...", end="")
