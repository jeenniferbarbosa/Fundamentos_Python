peso = float(input("Qual é seu peso atual? "))
altura = float(input("Qual é sua altura atual? "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}. Você está ABAIXO DO PESO.")
elif imc < 25:
    print(f"Seu IMC é de {imc:.2F}. Você está no PESO IDEAL.")
elif imc < 30:
    print(f"Seu IMC é de {imc:.2F}. Você está em SOBREPESO.")
elif imc < 40:
    print(f"Seu IMC é de {imc:.2F}. Você está em OBESIDADE.")
else:
    print(f"Seu IMC é de {imc:.2F}. Você está em OBESIDADE MÓRBIDA.")