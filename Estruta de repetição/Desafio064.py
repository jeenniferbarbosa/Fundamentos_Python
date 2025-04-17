soma = 0
total_num = 0
num = int(input("Digite um número inteiro (999 para sair): "))

while True:
    soma += num
    total_num += 1
    num = int(input("Digite um número inteiro (999 para sair): "))
    if num == 999:
        print(f"O programa foi finalizado e você informou {total_num} digitos, a soma entre esses valores é: {soma}")