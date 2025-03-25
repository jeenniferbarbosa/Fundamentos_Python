# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual é a velocidade atual do carro? "))
multa = (velocidade - 80) * 7

print("A velocidade máxima da via é 80Km/h")

if velocidade <= 80:
    print("Você está dentro do limite. Boa viajem!")
else:
    print(f"Você ultrapassou o limite da via, por isso, será multado em R$ {multa:.2f}.")