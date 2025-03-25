import random

nomes = input("Digite os nomes dos 4 alunos separados com espaços: ")
alunos = nomes.split()
random.shuffle(alunos)
print(f"A ordem de apresentação será: {alunos} ")
