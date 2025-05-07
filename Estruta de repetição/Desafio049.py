print("TABUADA")

num = int(input("Digite um número e veja sua tabuada: "))

print("==" * 8)

for c in range(0, 11):
    mult = num * c
    print(f"{num} * {c} = {mult}")

print("==" * 8)
