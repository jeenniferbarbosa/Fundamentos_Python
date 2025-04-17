# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

total_num = 0
soma = 0
retorno = "S"
maior = menor = 0
while retorno == "S":
    num = int(input("Digite um valor: "))
    retorno = str(input("Quer continuar? [S/N]: ")).upper().strip()
    total_num += 1
    soma += num
    if total_num == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / total_num
print(f"Você informou {total_num} digítos. A média desses valores é: {media:.2f}.")
print(f"O maior o número informado foi {maior} e o menor foi {menor}.")
print("Fim do programa! Obrigada.")