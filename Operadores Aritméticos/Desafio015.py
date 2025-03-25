## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugado = int(input("Por quantos dias o carro foi alugado? "))
kmPercorrido = float(input("Qual o KM percorrido durante o aluguel? KM "))
valorFinal = (diasAlugado * 60) + (kmPercorrido * 0.15)

print(f"Durante os {diasAlugado} dias alugados, foram percorridos {kmPercorrido}km. Nisso, o valor total a ser pago é de R$ {valorFinal:.2f}")