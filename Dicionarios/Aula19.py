pessoas = {'nome': "Gustavo", 'sexo': 'M', 'idade': 22}
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 25.5

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

for k, v in pessoas.items():
    print(f"{k} = {v}")

#Lista com dicionários
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigle': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigle': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)