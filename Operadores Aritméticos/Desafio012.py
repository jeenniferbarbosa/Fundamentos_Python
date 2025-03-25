## Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input("Qual é o valor deste produto? R$ "))
desconto = valorProduto - (valorProduto * 0.05)

print(f"O produto de R$ {valorProduto} reais ficará R$ {desconto} com 5% de desconto.")