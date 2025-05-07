valores = ()

for n in range(0, 4):
    num = int(input((f"Informe o {n + 1}ª número: ")))
    valores += (num,)
print(f"O valor 9 apareceu {valores.count(9)} vez(es)")

if 3 in valores:
    print(f"O valor 3 está na posição {valores.index(3) + 1}")
else:
    print("O valor 3 não foi digitado.")

pares = [n for n in valores if n % 2 == 0]
if pares:
    print(f"Os valores pares digitados foram: {pares}")
else:
    print("Não foram digitados números pares")