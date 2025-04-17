soma = 0
while True:
    num = int(input("Informe um número (999 para finalizar): "))
    if num == 999:
        break
    soma += num
print(f"A soma dos valores digitas foi: {soma}.")
print("Fim do programa.")