import random

nomes = input("Digite os nomes dos 4 alunos separados com espaços: ")
alunos = nomes.split()
sortedo = random.choice(alunos)
print(f"Os nomes digitados foram: {alunos}")
print(f"O aluno (a) sorteado é {sortedo}")