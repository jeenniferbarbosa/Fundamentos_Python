lanche = ('Habúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Utilizando o range
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for comida in lanche:
    print(f"Eu vou comer {comida}")

# Usando o enumerate, dará a posição e precisa conter duas variáveis no FOR
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("Comi pra caramba!")

# Mostra a tupla em ordem
print(sorted(lanche))

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# print(len(c))
# print(c.count(5)) # vezes que o item apareceu
# print(c.index(2)) # em que posição está o item
del(lanche) # apaga da memória