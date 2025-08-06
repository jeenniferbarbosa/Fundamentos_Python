dados = dict()

dados['nome'] = str(input("Nome do aluno: "))
dados['media'] = float(input(f"Média de {dados['nome']}: "))

if dados['media'] >= 7:
    dados['situacao'] = "APROVADO"
elif 5 <= dados['media'] < 7:
    dados['situacao'] = "RECUPERAÇÃO"
else:
    dados['situacao'] = "REPROVADO"

print("==" * 12)
print(f"Nome: {dados['nome']}\nMédia: {dados['media']}\nSituação: {dados['situacao']}")
print("==" * 12)