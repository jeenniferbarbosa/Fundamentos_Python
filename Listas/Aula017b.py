valores = list()
# valores.append(6)
# valores.append(2)
# valores.append(9)

for cont in range(0,5):
    valores.append(int(input(f"Digite o {cont + 1}ª valor: ")))

print("====" * 12)
for c, v in enumerate(valores):  #enumerate percorre as chaves e os valores
    print(f"Na posição {c} encontrei o valor {v}")
print("====" * 12)

print("Fim da lista")