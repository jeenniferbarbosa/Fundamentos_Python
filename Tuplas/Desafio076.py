lista = ("Lápis", 1.75,
         "Borracha", 0.50,
         "Caderno", 50,
         "Grampeador", 10.50,
         "Cola", 2.00,
         "Mochila", 150.00,
         "Estojo", 30.98)

print("--" * 20)
print(f'{"LISTA DE PREÇOS":^40}') # Centralizado com 40 caractres
print("--" * 20)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f"{lista[posicao]:.<30}", end="") #30 caracteres e alinhado a esquerda
    else:
        print(f"R$ {lista[posicao]:>7.2f}")
print("--" * 20)