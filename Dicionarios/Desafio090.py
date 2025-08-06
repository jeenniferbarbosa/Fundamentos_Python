# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['nome'] = str(input("Nome do aluno: "))
dados['media'] = float(input("Média do aluno: "))

if dados['media'] <= 7:
    dados['situacao'] = "RECUPERAÇÃO"
else:
    dados['situacao'] = "APROVADO"

print("==" * 10)
print(f"Nome: {dados['nome']}\nMédia: {dados['media']}\nSituação: {dados['situacao']}")
print("==" * 10)