# MAIOR E MENOR PESO

menor = float('inf')  # Valor infinito (positivo)
maior = float('-inf')  # Valor infinito (negativo)

for pessoas in range(0, 6):
    peso = float(input(f"Informe o peso da {pessoas + 1}º pessoa: "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f"O maior peso informado foi: {maior}kg")
print(f"O menor peso informado foi: {menor}kg")