# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input("Digite um número de 0 a 9999: "))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10

print(f"""O número digitado é {num}.
Sua unidade é: {uni} 
Sua dezena é: {dez}
Sua centena é: {cent}
Sua milhar é: {mil}""")