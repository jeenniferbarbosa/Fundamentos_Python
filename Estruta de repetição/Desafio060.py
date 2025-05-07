## Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

## USANDO WHILE
num = int(input("informe um número e veja seu fatorial: "))
cont = num
fator = 1

print(f"Calculando {num}! = ", end='')

while cont > 0:
    print(f"{cont}", end='')
    print(f" x " if cont > 1 else " = ", end='')
    fator *= cont
    cont -= 1
print(fator)

## USANDO FOR
num = int(input("informe um número e veja seu fatorial: "))
fator = 1

for cont in range(num, 0, -1):
    print(f"{cont}", end='')
    print(f" x " if cont > 1 else " = ", end='')
    fator *= cont

print(f"{fator}")