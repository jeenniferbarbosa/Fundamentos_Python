soma = 0
cont = 0

while True:
    num = int(input("Informe um número (999 para finalizar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Foram informados {cont} valores, soma de todos eles será: {soma}.")
print("Fim do programa.")