# MAIORIDADE

from datetime import date

maiores = 0
menores = 0
anoAtual = date.today().year

for pessoa in range(0, 6):
    anoNasc = int(input(f"Qual o ano de nascimento da {pessoa + 1}ª pessoa: "))
    idade = anoAtual - anoNasc

    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f"{menores} pessoa(s) são menores de idade.")
print(f"{maiores} pessoas(s) são maiores de idade.")