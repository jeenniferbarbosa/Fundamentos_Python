print(" >>>>>> LOJAS BARBOSA <<<<<<<")
valorCompra = float(input("Qual o valor total das compras? R$ "))
print("""Escolha uma opção para pagamento: 
[1] à vista dinheiro/cheque: 10% de desconto 
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros """)

opcao = int(input("Opção desejada: "))

if opcao == 1:
    valorFinal = valorCompra - (valorCompra * 0.1)
    print(f" Pagando à vista, sua compra no valor de R$ {valorCompra:.2f} com 10% de desconto ficará R$ {valorFinal:.2f} reais.")
elif opcao == 2:
    valorFinal = valorCompra - (valorCompra * 0.05)
    print(f"Pagando à vista no cartão, sua compra no valor de R$ {valorCompra:.2f} com 5% de desconto ficará R$ {valorFinal:.2f} reais.")
elif opcao == 3:
    print(f"Não é possível conceder desconto parcelando 2x no cartão. O valor final de sua compra será de R$ {valorCompra:.2f} reais.")
elif opcao == 4:
    valorFinal = valorCompra + (valorCompra * 0.2)
    print(f"Parcelando 3x ou mais no cartão, sua compra terá juros de 20%. Sua compra passará de R$ {valorCompra:.2f} reais para R$ {valorFinal:.2f} reais.")
else:
    print("Opçao inválida! Tente novamente.")
