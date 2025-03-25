#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
#  e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Qual é o valor da casa? R$ "))
salario = float(input("Qual é valor do seu salário? "))
parcela = int(input("Em quantos anos você gostaria de pagar? "))
prestacao = valorCasa / (parcela * 12)

print(f"A prestação do seu imóvel ficará: R$ {prestacao:.2f} reais.")

if prestacao > (salario * 0.30):
    print("Seu empréstimo foi NEGADO, pois, a prestação mensal excede o limite de 30% acima do seu salário.")
else:
    print("PARABENS! Seu empréstimo foi aprovado.")