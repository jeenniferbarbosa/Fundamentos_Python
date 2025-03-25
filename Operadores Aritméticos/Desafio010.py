# Conversor de Moedas

dinheiro = float(input("Quanto de dinheiro você tem de dinheiro? R$ "))
dolar = dinheiro / 6.04

if dinheiro >= dolar:
    print("Infelizmente, com esse valor você não consegue comprar dólar.")

else:
    print(f"Com R$ {dinheiro:.2f} você consegue comprar US$ {dolar:.2f} dólar.")