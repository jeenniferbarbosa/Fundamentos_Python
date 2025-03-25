# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual é a distância em km/h para o seu destino? "))

if distancia <= 200:
    passagemA = 0.50 * distancia
    print(f"Sua viagem de {distancia} custará R$ {passagemA:.2f} reais.")
else:
    passagemB = 0.45 * distancia
    print(f"Sua viagem de {distancia} custará R$ {passagemB:.2f} reais.")
print("Boa viagem!")