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