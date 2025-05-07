num = [2, 5, 9, 1]
num[2] = 3 # Altera o valor do indice informado
num.append(7) # Adiciona um valor
num.sort() # Organiza
# num.insert(2, 0) # Insere na posicao informada um valor
# num.pop() # Elimina o ultimo valor da lista
num.insert(2,2)
if 4 in num:
    num.remove(2)
else:
    print("Não encontrei esse valor")
print(num)
print(f"Essa lista tem {len(num)} elementos. ")