num = ([], ([]))
valor = 0

for cont in range(0, 7):
    valor = int(input(f"Informe o {cont +1}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f"Os números pares são: {num[0]}.")
print(f"Os númereos impares são: {num[1]}.")