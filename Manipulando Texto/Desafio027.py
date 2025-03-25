nome = str(input("Digite seu nome: ")).strip()
nomeDiv = nome.split()
print(f"""Seu nome inteiro é: {nome}
Seu primeiro nome é {nomeDiv[0]}
Seu último nome é {nomeDiv[len(nomeDiv)-1]}""")