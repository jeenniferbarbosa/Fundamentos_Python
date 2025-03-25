# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

frase = str(input("Digite um frase: ")).strip().upper()

print(f"""Na frase '{frase}' possui {frase.count('A')} letra(s) 'A'.
A primeira letra A aparece na posição {frase.find('A')+1}.
A última letra A aparece na posição {frase.rfind('A')+1}""")