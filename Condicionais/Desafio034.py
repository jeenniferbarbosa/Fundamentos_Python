# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00,  calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salarioAtual = float(input("Qual é o salário atual do funcionário? "))

if salarioAtual > 1250.00:
    reajusteSalario = salarioAtual + ( salarioAtual * 0.10)
    print(f"O salário de R$ {salarioAtual:.2f} teve um reajuste de 10%, passando a ser R$ {reajusteSalario:.2f} ")
else:
    reajusteSalario = salarioAtual + (salarioAtual * 0.15)
    print(f"O salário de R$ {salarioAtual:.2f} teve um reajuste de 15%, passando a ser R$ {reajusteSalario:.2f} ")
print("Obrigada por utilizar nosso serviços!")